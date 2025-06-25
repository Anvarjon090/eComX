from django import forms
from django.contrib.auth import password_validation

from .models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput,
        help_text="Enter the same password as above, for verification.",
    )

    class Meta:
        model = User
        fields = ("email", "phone_number", "first_name", "last_name")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "email",
            "phone_number",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
        )


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()


class PasswordResetForm(forms.Form):
    email = forms.EmailField()


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "phone_number", "first_name", "last_name")
