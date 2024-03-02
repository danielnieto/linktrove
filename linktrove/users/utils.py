from .models import User


def get_user_display(user: User):
    return user.email
