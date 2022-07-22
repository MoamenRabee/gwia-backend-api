import imp
from logging import exception
from .serializer import PersonSerializers, MessageSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Person, PersonMessage
import requests


@api_view(['POST'])
def create_person(request):
    if request.method == 'POST':
        serializer = PersonSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "user created",
                "data": serializer.data
            }
            # Created
            return Response(response)
        # Not Valid
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    # Method Not Post
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'PUT'])
def get_person(request, username):
    try:
        person = Person.objects.get(username__exact=username)

    except:
        return Response({"message": "User Not Found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PersonSerializers(person)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PersonSerializers(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # Method Not Post
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def get_person_by_code(request, code):
    try:
        person = Person.objects.get(code__exact=code)
    except:
        return Response({"message": "User Not Found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PersonSerializers(person)
        return Response(serializer.data)
    # Method Not Post
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


# messages

@api_view(['POST'])
def new_message(request):
    if request.method == 'POST':
        serializer = MessageSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "message added",
                "data": serializer.data
            }

            # Created
            return Response(response)
        # Not Valid
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    # Method Not Post
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def get_my_messages(request, username):
    if request.method == 'GET':
        messages = PersonMessage.objects.filter(
            receiver_username=username).order_by("-created_date")
        serializer = MessageSerializers(messages, many=True)
        return Response(serializer.data)
    # Method Not Post
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def get_my_send_messages(request, username):
    if request.method == 'GET':
        messages = PersonMessage.objects.filter(
            sender_username=username).order_by("-created_date")
        serializer = MessageSerializers(messages, many=True)
        return Response(serializer.data)
    # Method Not Post
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)
