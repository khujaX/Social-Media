from rest_framework import permissions


class CanUpdateProfile(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if (request.user.is_authenticated and obj == request.user) or request.user.is_superuser:
            return True
        return False


class IsPublisherOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.publisher == request.user


class IsLiker(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.liker == request.user


class IsFollowerOrFollowing(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.follower == request.user or obj.following == request.user:
            return True
        return False


class IsCommenter(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.wtiter == request.user