from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_api_key.permissions import HasAPIKey

from generic_app.rest_api.views.permissions.UserPermission import UserPermission
from django.http import JsonResponse
from generic_app import generic_models

class Widgets(APIView):
    http_method_names = ['get']
    permission_classes = [HasAPIKey | IsAuthenticated]

    def get(self, *args, **kwargs):
        return JsonResponse({"widget_structure": generic_models.widget_structure})
