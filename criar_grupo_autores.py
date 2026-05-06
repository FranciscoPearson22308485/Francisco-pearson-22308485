import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from artigos.models import Artigo, Comentario, Like

# Criar grupo autores
grupo, created = Group.objects.get_or_create(name='autores')
print(f"Grupo 'autores': {'criado' if created else 'ja existe'}")

# Permissoes de Artigo
ct_artigo = ContentType.objects.get_for_model(Artigo)
perms_artigo = Permission.objects.filter(content_type=ct_artigo)
for p in perms_artigo:
    grupo.permissions.add(p)
    print(f"  + {p.codename}")

# Permissoes de Comentario
ct_com = ContentType.objects.get_for_model(Comentario)
perms_com = Permission.objects.filter(content_type=ct_com)
for p in perms_com:
    grupo.permissions.add(p)
    print(f"  + {p.codename}")

print(f"\nOK Grupo 'autores' tem {grupo.permissions.count()} permissoes!")
