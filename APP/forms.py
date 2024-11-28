from django import forms
from django.core.exceptions import ValidationError
from .models import User  
from django.forms.widgets import ClearableFileInput
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Password"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm Password"
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Username"
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        label="Email"
    )
    role = forms.ChoiceField(
        choices=User.role_choices,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Role"
    )
    profile_picture=forms.ImageField(
        widget=ClearableFileInput(attrs={'class':'form-control'}),
        label='Profile Picture'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password', 'role','profile_picture']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError("Passwords do not match!")

        return cleaned_data
    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        password = cleaned_data.get("password")
        user = super().save(commit=False)
        user.set_password(password)
        user.save()
        return user
    