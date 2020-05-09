from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse , HttpResponse
from .serializers import UserSerializer
from rest_framework import status
from django.contrib.auth.models import User
# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')
      

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        content = {
            'message': 'Token verified',
            'User Name': user.username,
            'Email': user.email,
            'FirstName': user.first_name,
            'LastName': user.last_name
        
        }
        return JsonResponse(content)

class UsersList(APIView):
    def get(self, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        users_list = list(serializer.data)
        return JsonResponse(users_list, safe=False)

class Register(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return JsonResponse(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return JsonResponse(
            {
                "error": True,
                "error_msg": 'serializer.error_messages',
            },
            status=status.HTTP_400_BAD_REQUEST
        )
