from django import forms
from django.contrib.auth import authenticate, login, get_user_model
from django import forms
from django.contrib.auth.models import User

User = get_user_model()


class GuestForm(forms.Form):
    email = forms.EmailField()


class LoginForm(forms.Form):
    # email = forms.EmailField(label='Email')
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "your full name"}))
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "your full name"}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control", "placeholder": "email"}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    def clean(self):
        data = self.cleaned_data
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('cpass')
        if password2 != password1:
            raise forms.ValidationError("Passwords should match")
        else:
            return data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email
