from rest_framework.permissions import BasePermission
from .models import Choices


class IsAdmin(BasePermission):
    ADMIN = Choices.ADMIN

    def has_permission(self, request, view):
        return request.user.role == self.ADMIN or request.user.is_superuser
