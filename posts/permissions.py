from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Authenticated users only can see list view
    Write permissions are only allowed to the author of a post
    """
    def has_permission(self, request, view):
        # Works with ListView
        # Authenticated users only can see list view
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # DetailView executes both has_permission and has_object_permission (in this order)
        # Read permissions are allowed to any request so we'll always
        # allow GET, HEAD, or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of a post
        return obj.author == request.user
