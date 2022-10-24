from django import forms
from django.forms import Form
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    email = forms.CharField(label='Почта', required=True, max_length=100)
    password = forms.CharField(label='Пароль', required=True, max_length=100)


class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder':'Имя'})
        self.fields['last_name'].widget.attrs.update({'placeholder':'Фамилия'})
        self.fields['email'].widget.attrs.update({'placeholder':'name@example.com'})
        self.fields['password1'].widget.attrs.update({'placeholder':'••••••••'})        
        self.fields['password2'].widget.attrs.update({'placeholder':'••••••••'})

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'country']
        labels = {  
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'country': 'Страна',
        }
        
