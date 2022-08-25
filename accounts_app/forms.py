from django import forms
from django.core.exceptions import ValidationError

from accounts_app.models import Account


class SignupForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['email', 'password', 'password2']
        widgets = {
            'email': forms.TextInput(attrs={
                'class': 'email-input',
                'type': 'email',
                'placeholder': "پست الکترونیک",
                'dir': 'ltr',
                'maxlength': '50',
                'required': '',
                'name': 'email'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'password-input',
                'dir': "ltr",
                'type': "password",
                'placeholder': "تکرار گذرواژه",
                'name': "password"
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'password-input',
                'dir': "ltr",
                'type': "password",
                'placeholder': "گذرواژه",
                'name': "password"
            })
        }

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

