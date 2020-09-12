from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class RegisterUser(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'error': None,
            'message': 'User Created Successfully'
        }, status.HTTP_201_CREATED)


class UserLogin(TokenObtainPairView):
    serializer_class = LoginSerializer
