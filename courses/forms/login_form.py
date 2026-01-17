from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if not email or not password:
            raise ValidationError("Email and password are required")

        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            raise ValidationError("Email or password invalid")

        user = authenticate(
            username=user_obj.username,
            password=password
        )

        if user is None:
            raise ValidationError("Email or password invalid")

        cleaned_data["user"] = user
        return cleaned_data