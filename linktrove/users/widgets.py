from django import forms


class CustomEmailWidget(forms.EmailInput):
    template_name = "users/widgets/email.html"


class CustomPasswordWidget(forms.PasswordInput):
    template_name = "users/widgets/password.html"
