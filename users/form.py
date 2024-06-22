from django import forms
from django.contrib.auth import get_user_model


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password_r = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'password_r']

    def clean_password_r(self):
        data = self.cleaned_data
        if data['password']!=data['password_r']:
            raise forms.ValidationError('Не совпадают пароли')
        return data['password']