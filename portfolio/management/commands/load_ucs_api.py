import requests
from django.core.management.base import BaseCommand
from portfolio.models import Licenciatura, UnidadeCurricular, Docente

class Command(BaseCommand):
    help = 'Importa Licenciatura e UCs da API da Lusófona - Informática de Gestão (código 12)'

    def handle(self, *args, **kwargs):
        url = 'https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetCourseDetail'
        
        self.stdout.write("A contactar a API da Lusófona...")
        
        try:
            r = requests.post(url,
                json={'language': 'PT', 'courseCode': 12, 'schoolYear': '202526'},
                headers={'content-type': 'application/json'})
            r.raise_for_status()
            d = r.json()
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Erro ao contactar API: {e}"))
            return

        # Criar Licenciatura com dados reais da API
        detail = d.get('courseDetail', {})
        licenciatura, created = Licenciatura.objects.get_or_create(
            sigla='IG',
            defaults={
                'nome': 'Informática de Gestão',
                'instituicao': 'Universidade Lusófona',
                'ano_inicio': 2023,
                'duracao_anos': 3,
                'url_pagina': 'http://informatica.ulusofona.pt/',
            }
        )
        self.stdout.write(f"Licenciatura: {'criada' if created else 'já existia'}")

        # Criar Docentes da API
        for teacher in d.get('teachers', []):
            nome = teacher.get('teacherName', '').strip()
            if nome:
                Docente.objects.get_or_create(
                    nome=nome,
                    defaults={
                        'email': teacher.get('teacherEmail', ''),
                        'url_pagina_lusofona': teacher.get('teacherUrl', ''),
                    }
                )

        # Criar UCs
        ucs = d.get('courseFlatPlan', [])
        criadas = 0
        for uc in ucs:
            nome = uc.get('curricularUnitName', 'Desconhecido')[:200]
            sigla = uc.get('curricularIUnitReadableCode', 'N/A')[:20]
            try:
                ects = int(uc.get('ects', 0))
                ano_curricular = int(uc.get('curricularYear', 1))
                semestre_raw = uc.get('semesterCode', 'S1')
                semestre = int(semestre_raw.replace('S', '')) if semestre_raw else 1
            except (ValueError, TypeError):
                ects, ano_curricular, semestre = 0, 1, 1

            _, created = UnidadeCurricular.objects.get_or_create(
                sigla=sigla,
                defaults={
                    'nome': nome,
                    'ano_curricular': ano_curricular,
                    'semestre': semestre,
                    'ects': ects,
                    'licenciatura': licenciatura,
                }
            )
            if created:
                criadas += 1

        self.stdout.write(self.style.SUCCESS(f"{criadas} UCs importadas de {len(ucs)} disponíveis na API!"))
