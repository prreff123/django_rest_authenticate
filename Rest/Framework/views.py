from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

@api_view(['GET'])
def book(reqeust):
    book_obj = Book.objects.all()
    serializer = bookserial(book_obj, many=True)
    return Response({'status':200,'payload': serializer.data})

class RegisterUser(APIView):
    def post(self,request):
        serializer = Userserial(data = request.data)
        if not serializer.is_valid():        
            return Response({'status':403,'errors': serializer.errors,'message':"Something went wrong!"})
        serializer.save()
        user = User.objects.get(username = serializer.data['username'])
        # token_obj = Token.objects.get_or_create(user=user)
        refresh = RefreshToken.for_user(user)

        return Response({'status':200,'payload': serializer.data,'refresh':str(refresh),'access': str(refresh.access_token),'message':"Your data is saved!"})

class StudentAPI(APIView):
    authentication_classes  = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        student_objs = student.objects.all()
        serializer = studentserial(student_objs, many=True)
        print(request.user)
        return Response({'status':200,'payload': serializer.data})

    def post(self,request):
            data = request.data
            serializer = studentserial(data=request.data)
            if not serializer.is_valid():
              print(serializer.errors)
              return Response({'status':403,'errors': serializer.errors,'message':"Something went wrong!"})
            serializer.save()
            return Response({'status':200,'payload': serializer.data,'message':"Your data is saved!"})
    
    def put(self,request):
        pass
    
    def patch(self,request):
        try:        
           student_obj = student.objects.get(id = request.data['id'])
           serializer = studentserial(student_obj,data=request.data, partial=False)
           if not serializer.is_valid():
              print(serializer.errors)
              return Response({'status':403,'errors': serializer.errors,'message':"Something went wrong!"})
           serializer.save()
           return Response({'status':200,'payload': serializer.data,'message':"Your data is updated!"})
        except Exception as e:
           print(e)
           return Response({'status':403,'message':"Invalid id!!"})

    def delete(self,request):
        try:
           id = request.GET.get('id')        
           student_obj = student.objects.get(id = id)
           student_obj.delete()
           return Response({'status':200,'message':"Deleted!"})

        except Exception as e:
           print(e)
           return Response({'status':403,'message':"Invalid id!!"})

