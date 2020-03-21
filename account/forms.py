from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='ユーザー名', max_length=100)
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput(), max_length=100)
    redirect_to = forms.CharField(widget=forms.HiddenInput)
