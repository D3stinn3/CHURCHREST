from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from accountapi.models import User
from rest_framework.views import APIView
from django.contrib.auth import logout


from accountapi.serializers import UserSerializer


class UserLoginView(APIView):

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, username=request.data['username'])
        if not user.check_password(request.data['password']):
            return Response({"Detail": "User Not Found"}, status=status.HTTP_404_NOT_FOUND)
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(instance=user)
        if user:
            if user.is_active:
                return Response({"message": "Success, BaseUser Logged In", "token": token.key, "user": serializer.data})
            return Response({"message": f"{str(user.username)} is not Active"})
        return Response(serializer.errors, status=status.HTTP_408_REQUEST_TIMEOUT)
    
userloginView = UserLoginView.as_view()

class UserLogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)

userlogoutView = UserLogoutView.as_view()

class UserSignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user_instance = serializer.save()
            user_instance.set_password(request.data['password'])
            user_instance.is_active = True
            user_instance.save()

            # Token Generated during SignUp
            token, created = Token.objects.get_or_create(user=user_instance)

            return Response(
                {"message": "Success, BaseUser Registered!", "token": token.key, "user": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
usersignupView = UserSignupView.as_view()