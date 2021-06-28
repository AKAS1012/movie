from rest_framework import permissions


class AdminOrReadOnly(permissions.IsAdminUser):
	def has_permission(self, request, view):
		if request.method and permissions.SAFE_METHODS:
			return True
		else:
			return bool(request.user and request.user_is_staff)


class ReviewUserOrReadOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.method and permissions.SAFE_METHODS:
			return True
		else:
			return obj.review.user == request.user
