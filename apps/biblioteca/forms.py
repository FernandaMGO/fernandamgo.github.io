from django import forms
from apps.biblioteca.models import Livro

class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Livro
        exclude = ['publicada',]
        labels = {
            "descricao": 'Descrição',
            'data_fotografia': "Data de Registro",
            'usuario': "Usuário",
            }
        widgets = {
            "animal": forms.TextInput(attrs={"class": "form-control"}),
            "autor": forms.TextInput(attrs={"class": "form-control"}),
            "legenda": forms.TextInput(attrs={"class": "form-control"}),
            "categoria": forms.Select(attrs={"class": "form-control"}),
            "descricao": forms.Textarea(attrs={"class": "form-control"}),
            "foto": forms.FileInput(attrs={"class": "form-control"}),
            "usuario": forms.Select(attrs={"class": "form-control"}),
            "data_fotografia": forms.DateInput(
                format="%d/%m/%Y",
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
            
        }

