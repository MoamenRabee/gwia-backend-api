from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Person, PersonMessage


class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class MessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = PersonMessage
        fields = '__all__'
