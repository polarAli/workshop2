from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import status

from .serializers import UserSerializer, LoginSerializer, UserUpdateSerializer


class LoginView(APIView):
    authentication_classes = [SessionAuthentication]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            user = authenticate(request=request,
                                username=serializer.validated_data['username'],
                                password=serializer.validated_data['password'])
            if user:
                login(request, user)
                return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'authentication failed!'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'message': 'validation failed!',
                             'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class SignupView(APIView):
    authentication_classes = [SessionAuthentication]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'You can login now!'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'validation failed!',
                             'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    authentication_classes = [SessionAuthentication]

    def put(self, request):
        serializer = UserUpdateSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'validation failed!',
                             'errors': serializer.errors
                             }, status=status.HTTP_400_BAD_REQUEST)


class UsersListView(APIView):
    authentication_classes = [SessionAuthentication]

    def get(self, request):
        users = User.objects.all()
        return Response(UserSerializer(users, many=True).data, status=status.HTTP_200_OK)
