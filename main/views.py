from django.shortcuts import render
from rest_framework import viewsets, status
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, CategorySerializer
from .models import User, Category

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if not username or not password:
        return Response({
            'message':'All fields are required'
        }, status = 400)
    user = authenticate(username = username, password = password)
    if user:
        return Response({
            'status':'successfull login', 
            'user_id':user.id,
            'username':user.username
        })
    else:
        return Response({
            'message':'Wrong password or login'
            
        })
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

