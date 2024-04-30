from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import Userserializers
from .serializers import Roleserializers
from .serializers import UserRoleserializer
from rest_framework.views import APIView
from django.http import JsonResponse
from django.contrib.auth import authenticate, login



class add(APIView):
    def post(self, request):
        serializer =Userserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class Update(APIView):
    def post(self, request, id):
        user=User.objects.get(User_id=id)
        serializer =Userserializers(instance=user, data=request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class Delete(APIView):
    def get(self, request, id):
        user=User.objects.get(User_id=id)
        user.delete()
        return Response('Deleted')

class UserLogin(APIView):
    def post(self, request):

        Username = request.data.get('Username')
        Password = request.data.get('Password')


        user = authenticate(request, Username=Username, Password=Password)
        if user is not None:
            try:

                user_role = UserRole.objects.filter(User_id=user).latest('id')
                if user_role.status == UserRole.ACTIVE:
                    login(request, user)
                    return Response( 'Login successful')
                else:

                    return Response('User is not active')
            except UserRole.DoesNotExist:

                return Response( 'User  not found')








