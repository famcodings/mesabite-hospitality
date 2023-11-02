from rest_framework.permissions import DjangoModelPermissions as BaseDjangoModelPermissions


class DjangoModelPermissions(BaseDjangoModelPermissions):
  
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# Overriding perms_map's GET key to enable view permissions
		# https://github.com/encode/django-rest-framework/blob/efc7c1d664e5909f5f1f4d07a7bb70daef1c396e/rest_framework/permissions.py#L175
		self.perms_map["GET"].append('%(app_label)s.view_%(model_name)s')

	def has_permission(self, request, view):
		if not request.user or not request.user.is_authenticated:
			return False

		if hasattr(view, 'custom_permissions') and view.custom_permissions and request.resolver_match.view_name in view.custom_permissions:
			return request.user.has_perm(view.custom_permissions[request.resolver_match.view_name])
		return super().has_permission(request, view)