from rest_framework.permissions import BasePermission

class IsPlatform_Manager(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == 'platform_manager'
        )


class IsOrganizer(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == 'organizer'
        )
    
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user
    

class IsEventOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user
