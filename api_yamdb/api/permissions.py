from rest_framework.permissions import (SAFE_METHODS, BasePermission,
                                        IsAuthenticatedOrReadOnly)


class IsAdminOrReadOnly(IsAuthenticatedOrReadOnly):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return (
                request.method in SAFE_METHODS
                or request.user.is_superuser
                or request.user.role == 'admin'
            )
        return request.method in SAFE_METHODS


class IsAccessEditPermission(IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return (
                request.method in SAFE_METHODS
                or request.user.is_superuser
                or request.user.role == 'admin'
                or request.user.role == 'moderator'
                or obj.author == request.user
            )
        return request.method in SAFE_METHODS


class IsAdminPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return (
                request.user.role == 'admin'
                or request.user.is_superuser
            )
