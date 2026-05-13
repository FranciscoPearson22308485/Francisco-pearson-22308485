"""
Script de migração de ficheiros locais (media/) para Cloudinary.

Utilização (após preencher as credenciais Cloudinary no .env):
    python manage.py shell < migra_ficheiros.py

Modelos migrados:
    - artigos.Artigo          → fotografia   (artigos/)
    - portfolio.Docente       → foto         (docentes/)
    - portfolio.UnidadeCurricular → imagem   (ucs/)
    - portfolio.Tecnologia    → logo         (tecnologias/)
    - portfolio.Projeto       → imagem       (projetos/)
    - portfolio.Formacao      → certificado  (certificados/)
    - portfolio.MakingOf      → foto         (makingof/)
    - escola_online.Curso     → imagem       (cursos/)
"""

import os
from django.core.files import File

from artigos.models import Artigo
from portfolio.models import Docente, UnidadeCurricular, Tecnologia, Projeto, Formacao, MakingOf
from escola_online.models import Curso

MEDIA_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media')


def migrar_campo(instancia, campo_nome, label):
    campo = getattr(instancia, campo_nome)
    if not campo or not campo.name:
        return False

    caminho_local = os.path.join(MEDIA_ROOT, campo.name)
    if not os.path.exists(caminho_local):
        print(f"  [SKIP] {label} #{instancia.pk}: ficheiro não encontrado → {caminho_local}")
        return False

    nome_ficheiro = os.path.basename(caminho_local)
    with open(caminho_local, 'rb') as f:
        getattr(instancia, campo_nome).save(nome_ficheiro, File(f), save=True)
    print(f"  [OK]   {label} #{instancia.pk}: {nome_ficheiro} → Cloudinary")
    return True


modelos = [
    (Artigo,              'fotografia',  'Artigo'),
    (Docente,             'foto',        'Docente'),
    (UnidadeCurricular,   'imagem',      'UnidadeCurricular'),
    (Tecnologia,          'logo',        'Tecnologia'),
    (Projeto,             'imagem',      'Projeto'),
    (Formacao,            'certificado', 'Formacao'),
    (MakingOf,            'foto',        'MakingOf'),
    (Curso,               'imagem',      'Curso'),
]

total_ok = 0
total_skip = 0

for modelo, campo, label in modelos:
    registos = modelo.objects.all()
    print(f"\n=== {label} ({registos.count()} registos) ===")
    for obj in registos:
        resultado = migrar_campo(obj, campo, label)
        if resultado:
            total_ok += 1
        else:
            total_skip += 1

print(f"\n{'='*50}")
print(f"Migração concluída: {total_ok} ficheiros enviados, {total_skip} ignorados.")
