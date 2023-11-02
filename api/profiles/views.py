from django.contrib.auth import get_user_model

from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from profiles.serializers import RegisterSerializer, UserSerializer

User = get_user_model()

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        user = serializer.save()
        return Response({"isRegistered": True}, status=status.HTTP_201_CREATED)


class Logout(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class UpdateProfileView(generics.GenericAPIView):

    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


    def put(self, request, format=None):
        try:
            update_user_serializer = self.get_serializer(request.user, data=request.data)
            if not update_user_serializer.is_valid():
                return Response(update_user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            user = update_user_serializer.save()
        except Exception as error:
            errors = {"error": str(error)}
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(self.get_serializer(user).data, status=status.HTTP_200_OK)