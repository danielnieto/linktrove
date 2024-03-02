from allauth.account.forms import (
    LoginForm,
    ResetPasswordKeyForm,
    ResetPasswordForm,
    SignupForm,
)
from .widgets import CustomEmailWidget, CustomPasswordWidget


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["login"].widget = CustomEmailWidget()
        self.fields["password"].widget = CustomPasswordWidget()


class CustomResetPasswordKeyForm(ResetPasswordKeyForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget = CustomPasswordWidget()
        self.fields["password2"].widget = CustomPasswordWidget()


class CustomResetPasswordForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget = CustomEmailWidget()


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget = CustomEmailWidget()
        self.fields["password1"].widget = CustomPasswordWidget()
        self.fields["password2"].widget = CustomPasswordWidget()
