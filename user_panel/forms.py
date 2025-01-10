from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class SignUpForm(forms.Form):
    fullname = forms.CharField(max_length=100, required=True)
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(max_length=254, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), validators=[validate_password])

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def save(self):
        fullname_parts = self.cleaned_data['fullname'].split(None, 1)
        first_name = fullname_parts[0]
        last_name = fullname_parts[1] if len(fullname_parts) > 1 else ""

        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            first_name=first_name,
            last_name=last_name,
            email=self.cleaned_data['email']
        )
        return user