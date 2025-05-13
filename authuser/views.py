from rest_framework import status, viewsets
from rest_framework.response import Response
from django.conf import settings
from django.utils import timezone
from .models import CustomUser 
from .serializers import LoginSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response 

class RegisterUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            return Response(
                {"message": "User created successfully. OTP sent to your email."},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password

class LoginViewSet(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            # Return specific error if username is incorrect
            return Response({
                "status": "failed",
                "message": "Username is incorrect"
            })
        

        if not check_password(password, user.password):
            # Return specific error if password is incorrect
            return Response({
                "status": "failed",
                "message": "Password is incorrect"
            })

        if user.is_email_verified == False:
            return Response({
                "status": "failed",
                "message": "Email is not verified"
            })

        refresh = RefreshToken.for_user(user)
        return Response ({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            "success": True,
            "message": "Login successfull"
        })