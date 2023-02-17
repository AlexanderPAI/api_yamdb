from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticatedOrReadOnly


class IsAdminPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_anonymous:
            return request.user.role == 'admin' or request.user.is_superuser


#class IsAdminOrReadOnly(IsAuthenticatedOrReadOnly):
#    def has_permission(self, request, view):
#        return request.method in SAFE_METHODS or request.user.is_superuser
#    def has_object_permission(self, request, view, obj):
#        return request.method in SAFE_METHODS or request.user.is_superuser
