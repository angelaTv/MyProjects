from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "your full name"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "your full name"}))


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "your full name"}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control", "placeholder": "email"}))
    dob = forms.DateField(widget=forms.DateInput(
        attrs={"class": "form-control", "placeholder": "dob"}))
    address = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "address"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "Password"}))
    cpass = forms.CharField(label='Confirm password', widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "Confirm Password"}))



    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        cpass = self.cleaned_data.get('cpass')
        if cpass != password:
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
