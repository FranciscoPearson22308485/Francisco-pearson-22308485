import json, os
from django.core.management.base import BaseCommand
from portfolio.models import TFC, Tecnologia

class Command(BaseCommand):
    help = 'Carrega TFCs do ficheiro data/tfcs.json'

    def handle(self, *args, **kwargs):
        json_path = os.path.join('data', 'tfcs.json')
        with open(json_path, encoding='utf-8') as f:
            data = json.load(f)

        criados = 0
        for item in data['tfcs']:
            tfc, created = TFC.objects.get_or_create(
                titulo=item.get('titulo', '')[:300],
                defaults={
                    'autor': ', '.join(item.get('autores', [])),
                    'orientador': ', '.join(item.get('orientadores', [])),
                    'ano': int(item.get('ano', 2025)),
                    'resumo': item.get('resumo', ''),
                    'url': item.get('link_pdf', ''),
                    'area': ', '.join(item.get('areas', [])),
                    'destacado': item.get('rating', 0) >= 4,
                }
            )
            for nome_tec in item.get('tecnologias', []):
                tec, _ = Tecnologia.objects.get_or_create(
                    nome=nome_tec,
                    defaults={'categoria': 'FE'}
                )
                tfc.tecnologias.add(tec)
            if created:
                criados += 1

        self.stdout.write(self.style.SUCCESS(f'{criados} TFCs carregados com sucesso!'))
