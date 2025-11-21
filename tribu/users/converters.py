from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class UserConverter:
    regex = r'\w+'

    def to_python(self, username: str) -> User:
        return get_object_or_404(User, username=username)

    def to_url(self, user: User) -> str:
        return user.username
