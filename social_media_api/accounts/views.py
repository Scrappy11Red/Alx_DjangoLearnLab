from django.shortcuts import render, redirect 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework import status, generics, permissions
from .models import CustomUser
from .serializers import UserSerializer
from django.contrib.auth import authenticate, login, logout

# Create your views here.
@api_view(['POST'])
def RegisterView(request):
    serializer = UserSerializer(data=request.data)
    template_name = "register.html"
    if serializer.is_valid():
        user = serializer.save()
        token = Token.objects.create(user=user)
        redirect("/")
        return Response({'token': str(token)}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def LoginView(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    error_messages = "Invalid password or username"
    if user is not None:
        login(request, user)
        redirect("/")
    else:
        return error_messages

def LogoutView(request):
    logout(request)
    redirect("login/")