from dataclasses import fields
from rest_framework import serializers
from .models import UserInput

operation=(
        ('addition','addition'),
        ('subtraction','subtraction'),
        ('multiplication','multiplication')
    )
class Serializer(serializers.Serializer):

   operation_type=serializers.ChoiceField(choices=operation)
   x=serializers.IntegerField()
   y=serializers.IntegerField()