from typing import Type
from rest_framework import serializers
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.db import IntegrityError
from rest_framework.renderers import JSONRenderer
from rest_framework import response
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.decorators import api_view
# from rest_framework.permissions import IsAuthenticated
from .models import  Designation, Followupcustomerdetails, User,Customerdetails,Status
#  Categorytype, Manpower, Manpowerdates, Natureofwork, Projectmanpower, Size,Category_Subtype,
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers

from django.contrib.auth.password_validation import validate_password
#-------------------------------------------user----------------------------------------------------------------------
class UserSerializer(serializers.ModelSerializer):

    # userdesignation = serializers.SerializerMethodField('get_designation') 
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance




class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    # old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}
        
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
    
    # def validate_old_password(self, value):
    
    #     user = self.context['request'].user
    #     if not user.check_password(value):
    #         raise serializers.ValidationError({"old_password": "Old password is not correct"})
    #     return value


    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()

        return instance



class DesignationSerialize(serializers.ModelSerializer):

    class Meta:
        model = Designation
        fields = ['id', 'designation']


#--------------------------------list users------------------------------------------

class ListuserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'name', 'email','username','designation']



#--------------------------------customer--------------------------------------------
class CustomerSerializer(serializers.ModelSerializer):

    telecallname=serializers.SerializerMethodField('get_telecallname')
    statusname=serializers.SerializerMethodField('get_statusname')

    class Meta:
        model = Customerdetails
        fields =['id','name','phone','religion',
        'cast','district','feedback',
        'gender','age','status','statusname','remarks',
        'followup','telecall','telecallname','flag']


    def get_telecallname(self, obj):
        return obj.telecall.name

    def get_statusname(self, obj):
        return obj.status.status_value
#--------------------------------------------designation--------------------------------------------------
class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields =['id','status_value']
#-----------------------------------------------------followup----------------------------------------------   
class FollowupcustomerdetailsSerializer(serializers.ModelSerializer):


    class Meta:
        model = Followupcustomerdetails
        fields =['id','name','phone','religion','cast','district','feedback','gender','age','status','remarks','followup','telecall','flag','is_followup']

