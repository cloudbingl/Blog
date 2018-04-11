from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username,password=password)
        if user is None:
            raise forms.ValidationError("用户名或密码错误")
        else:
            self.cleaned_data['user'] = user

        return self.cleaned_data


class RegisterForm(forms.Form):
    pass