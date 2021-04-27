from rest_framework import permissions
from users.models import Choices


class IsSuperuserPermissionOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_superuser
        )


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_anonymous:
            return (
                obj.author == request.user
                or request.user.is_superuser
                or request.user.role == Choices.ADMIN
                or request.user.role == Choices.MODERATOR
            )
        return request.method in permissions.SAFE_METHODS
