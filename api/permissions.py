from rest_framework.permissions import BasePermission

class IsAdminUserCustom(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class IsPremiumUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.account_tier in ["PREMIUM", "UNLIMITED"]
