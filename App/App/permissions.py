from rest_framework.permissions import BasePermission


class IsOwnerOrSuperUser(BasePermission):
    """
    Object-level permission to only allow superusers and owners of an object to edit and view it.
    Assumes the model instance has an `created_by` attribute.
    """

    edit_methods = ("GET", "PUT", "DELETE")

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        
        if request.user.is_superuser:
            return True

        # Instance must have an attribute named `created_by`.
        return obj.created_by == request.user
