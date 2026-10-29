from django import forms

from .models import Voluntario


class VoluntarioForm(forms.ModelForm):
    # o html do formulario e montado a mao em voluntario.html (pra manter o layout),
    # entao os nomes dos campos aqui precisam ser iguais aos name="" de la
    class Meta:
        model = Voluntario
        fields = ['nome', 'telefone', 'email', 'periodo', 'projetos', 'horas']
        widgets = {
            'periodo': forms.RadioSelect,
            'projetos': forms.CheckboxSelectMultiple,
        }
        error_messages = {
            'projetos': {'required': 'Escolha pelo menos um projeto.'},
        }
