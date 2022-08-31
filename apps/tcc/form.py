from django import forms
from .models import Autor, Orientador, Tcc, Usuario, Curso

class AutorForm(forms.ModelForm):

    data_nasc = forms.DateField(
        label='Data de nascimento',
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
            }),
        input_formats=('%Y-%m-%d',),
    )

    class Meta:
        model = Autor
        fields = "__all__"

class TccForm(forms.ModelForm):

    class Meta:
        model = Tcc
        fields = "__all__"
        exclude = ('usuario',)

class OrientadorForm(forms.ModelForm):

    data_nasc = forms.DateField(
        label='Data de nascimento',
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
            }),
        input_formats=('%Y-%m-%d',),
    )

    class Meta:
        model = Orientador
        fields = "__all__"

class UsuarioForm(forms.ModelForm):

    data_nasc = forms.DateField(
        label='Data de nascimento',
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'type': 'date',
            }),
        input_formats=('%Y-%m-%d',),
    )

    class Meta:
        model = Usuario
        fields = "__all__"

class CursoForm(forms.ModelForm):

        

    class Meta:
        model = Curso
        fields = "__all__"