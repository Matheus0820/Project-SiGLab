from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Bolsista

class FormUser(UserCreationForm):
    class Meta:
        model = User 
        fields = ('first_name', 'last_name', 'password1', 'password2', 'username', 'email',)
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sobrenome'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme a senha'}), 
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

class FormEditUser(UserChangeForm):
    class Meta:
        model = User 
        fields = ('first_name', 'last_name', 'username', 'email',)
        exclude = ('password',)
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sobrenome'}), 
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

class FormPasswordUser(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Senha Antiga'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nova Senha'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirmar Nova Senha'})


class FormBolsista(forms.ModelForm):
    class Meta:
        model = Bolsista
        fields = ('matricula', 'cpf', 'curso', 'grauEscolar', 'tipoDeBolsa',)
        widgets = {
            'matricula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Matrícula'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CPF', 'onfocus': 'formatarCPF(this.id)'}),
            'curso': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Curso'}),
            'grauEscolar': forms.Select(attrs={'class': 'form-control'}), 
            'tipoDeBolsa': forms.Select(attrs={'class': 'form-control'}),
        }

