
from rest_framework import generics
from rest_framework import response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from callcenterapp import serializers
from .models import *
from .serializers import *

from callcenterapp.serializers import CustomerSerializer, StatusSerializer, UserSerializer
from .models import Customerdetails, Status, User
# Create your views here.
#permisson_classes =[IsAuthenticated]  
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.decorators.csrf import requires_csrf_token
from django.shortcuts import render


import datetime
from django.conf import settings
import pandas as pd
import uuid
# from django.views.decorators.csrf import csrf_exempt

import os
import glob


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"status": True, "message": "Success", "response": serializer.data['id']})
        return Response({"status": False, "message": "failed", "response": serializer.errors})


class ChangePasswordView(APIView):


    serializer_class = ChangePasswordSerializer
    def put(self, request, pk):
        ser = User.objects.get(id=pk)
        serializer = ChangePasswordSerializer(instance=ser,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"status": True, "message": "Updated", "response": "ok"})
        return Response({"status": False, "message": serializer.error_messages, "response": serializer.errors})
        print(Response)



# --------------------------------list users------------------------------------------
class Listdesignation(generics.GenericAPIView):
    permisson_classes =(IsAuthenticated, ) 
    serializer_class=DesignationSerialize        
    def get(self, request):
        queryset = Designation.objects.all()
        serializer = DesignationSerialize(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})



class Listuserss(generics.GenericAPIView):

    serializer_class = ListuserSerializer

    def get(self, request):
        queryset = User.objects.all()
        serializer = ListuserSerializer(queryset, many=True)
        return Response(serializer.data)


class Getuserbyid(generics.GenericAPIView):

    serializer_class = ListuserSerializer

    def get(self, request, pk):
        queryset = User.objects.get(id=pk)
        serializer = ListuserSerializer(queryset, many=False)
        return Response(serializer.data)


class Updateuser(generics.UpdateAPIView):

    serializer_class = ListuserSerializer

    def put(self, request, pk):
        des = User.objects.get(id=pk)
        ser = ListuserSerializer(instance=des, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response("Updated!!")
        return Response({"status": False, "message": "failed" ,"response": ser.errors})




#-------------------------------------login#----------------------------------------------------------
class Login(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        response = Response()
        

        response.data = {

            "status":True,
            "message":'Success',
            "id":user.id,
            "email":user.email,
            "name":user.name
        }
        return response


#-----------------------------------------------------list customer details------------------------

class ListCustomerdetails(generics.GenericAPIView):
    permisson_classes =(IsAuthenticated, ) 
    serializer_class=CustomerSerializer        
    def get(self, request):
        queryset = Customerdetails.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})

#-----------------------------------------------------list customer details------------------------
class ListStatus(generics.GenericAPIView):
    permisson_classes =(IsAuthenticated, ) 
    serializer_class=StatusSerializer        
    def get(self, request):
        queryset = Status.objects.all()
        serializer = StatusSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})

#-------------------------------------------------------add form------------------------------------

class AddCustomerdetails(generics.CreateAPIView):
    permisson_classes =(IsAuthenticated, )        
    serializer_class=CustomerSerializer        
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})
        return Response({
            "status":False,
            "message":'failed',
            "response":serializer.errors})

class Getcustomerbyid(generics.GenericAPIView):

    serializer_class = CustomerSerializer

    def get(self, request, pk):
        queryset = Customerdetails.objects.get(id=pk)
        serializer = CustomerSerializer(queryset, many=False)
        return Response(serializer.data)

#--------------------------------------------------------patch customer details------------------------

class PatchCustomerdetails(generics.UpdateAPIView):
    permisson_classes =(IsAuthenticated, ) 
    serializer_class = CustomerSerializer

    def put(self, request, pk):
        des = Customerdetails.objects.get(id=pk)
        ser = CustomerSerializer(instance=des, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"status": True, "message": "Updated", "response": ser.data})
        return Response({"status": False, "message": "Updated", "response": ser.errors})

class Deletecustomer(generics.DestroyAPIView):

    serializer_class = CustomerSerializer

    def delete(self, request, pk):
        des = Customerdetails.objects.get(id=pk)
        des.delete()
        return Response("Deleted!!")
#--------------------------------------------------followup---------------------------------



class AddFollowupcustomerdetails(generics.CreateAPIView):
    permisson_classes =(IsAuthenticated, )        
    serializer_class=FollowupcustomerdetailsSerializer        
    def post(self, request):
        serializer = FollowupcustomerdetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": True, "message": "Updated", "response": serializer.data})
        return Response({"status": False, "message": "Updated", "response": serializer.errors})


class ListFollowupcustomerdetails(generics.GenericAPIView):
    permisson_classes =(IsAuthenticated, ) 
    serializer_class=FollowupcustomerdetailsSerializer        
    def get(self, request):
        queryset = Followupcustomerdetails.objects.all()
        serializer = FollowupcustomerdetailsSerializer(queryset, many=True)
        return Response({
            "status":True,
            "message":'Success',
            "response":serializer.data})
            

class PatchFollowupcustomerdetails(generics.UpdateAPIView):
    permisson_classes =(IsAuthenticated, ) 
    serializer_class = FollowupcustomerdetailsSerializer

    def put(self, request, pk):
        des = Followupcustomerdetails.objects.get(id=pk)
        ser = FollowupcustomerdetailsSerializer(instance=des, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"status": True, "message": "Updated", "response": ser.data})
        return Response({"status": False, "message": "Updated", "response": ser.errors})
         
#-----------------------------------------------------export-----------------------------------------------
class ExportExcel(APIView):
    def get(self, request):
        student_obj =Customerdetails.objects.all()
        serializer =CustomerSerializer(student_obj, many=True)
        df = pd.DataFrame(serializer.data)
        print(df)
        df.to_csv(f"public/static/excel/{uuid.uuid4()}.csv" ,encoding="UTF-8" , index=False)
        return Response({"status":"exported"})

#-----------------------------------------------------import-----------------------------------------
class ImportExcel(APIView):
    def post(self, request):
        path = os.getcwd()
        excel_upload_obj=ExcelFileupload.objects.create(excel_file_upload=request.FILES['files'])
        #df = pd.read_csv(f"{settings.BASE_DIR}excel/{excel_upload_obj.excel_file_upload}")       
        df = pd.read_csv(f"{excel_upload_obj.excel_file_upload}")
        for student in (df.values.tolist()):
            Customerdetails.objects.create(
                name =student[1],
                phone=student[2],
                religion=student[3],
                cast=student[4],
                district =student[5],
                gender=student[7],
                feedback=student[6],
                age=student[8],
                # status=Status.objects.get(id=student[9]),
                # remarks =student[10],
                # followup=student[11],
                telecall=User.objects.get(id=student[12]),
            )            
            print(student)
        return Response({"status": True, "message": "Imported", "response": "success"})
        
        
        
# class ImportExcel(APIView):
#     def post(self, request):
#         excel_upload_obj=ExcelFileupload.objects.create(excel_file_upload=request.FILES['files'])
#         df = pd.read_csv(f"{settings.BASE_DIR}excel/{excel_upload_obj.excel_file_upload}")
#         for student in (df.values.tolist()):
#             Customerdetails.objects.create(
#                 name =student[1],
#                 phone=student[2],
#                 religion=student[3],
#                 cast=student[4],
#                 district =student[5],
#                 gender=student[7],
#                 feedback=student[6],
#                 age=student[8],
#                 # status=student[9],
#                 # remarks =student[10],
#                 # followup=student[11],
#                 assignedto=student[12],
#             )            
#             print(student)
#         return Response({"status":"Imported","response":"student"})
  
