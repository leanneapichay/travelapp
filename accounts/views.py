from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class Login(APIView):

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = IsAuthenticated

    def get(self, request, format=None):
        content = {
            'user': request.user,
            'auth': request.auth
        }
        return Response(content)
