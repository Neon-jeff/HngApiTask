from dataclasses import fields
from rest_framework import serializers
from .models import UserInput

class Serializer(serializers.ModelSerializer):
    class Meta:
        model=UserInput
        fields='__all__'