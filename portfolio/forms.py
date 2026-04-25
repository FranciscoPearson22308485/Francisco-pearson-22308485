from django import forms
from .models import Projeto, Tecnologia, Competencia, Formacao

# Formulário para os Projetos
class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__' # Cria os campos todos automaticamente baseados no modelo

# Formulário para as Tecnologias
class TecnologiaForm(forms.ModelForm):
    class Meta:
        model = Tecnologia
        fields = '__all__'

# Formulário para as Competências
class CompetenciaForm(forms.ModelForm):
    class Meta:
        model = Competencia
        fields = '__all__'

# Formulário para as Formações
class FormacaoForm(forms.ModelForm):
    class Meta:
        model = Formacao
        fields = '__all__'