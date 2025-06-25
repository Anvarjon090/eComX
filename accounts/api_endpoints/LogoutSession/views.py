from django.contrib.auth import logout
from rest_framework.views import APIView
from django.http import JsonResponse


class SessionLogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return JsonResponse({"message": "Logout successful"})


__all__ = ["SessionLogoutAPIView"]
