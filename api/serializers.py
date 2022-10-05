from __future__ import division

import datetime

from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_jwt.serializers import JSONWebTokenSerializer

from api.models import *

class JWTSerializer(JSONWebTokenSerializer):
    def validate(self, attrs):
        validated_data = super().validate(attrs)
        update_last_login(None, validated_data["user"])
        return validated_data

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "username", "account_type", 
                  "first_name", "password", 
                  "contact", "last_name", "date_of_birth", "gender",
                  "home_address", "occupation")

class UserSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        rep = super(UserSerializer, self).to_representation(instance)
        rep.pop("password", None)
        return rep

    class Meta:
        model = User
        fields = "__all__"
        write_only_fields = ("password",)

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=120)
    new_password = serializers.CharField(max_length=120)

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"

class RecruitmentAgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitmentAgency
        fields = "__all__"

