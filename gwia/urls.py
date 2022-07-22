from django.urls import path
from . import views, api
urlpatterns = [
    path('', views.index, name='index'),
    path('message/<username>', views.send_message, name='send_message'),



    # API
    # create person
    path('api/person/create', api.create_person, name='create_person'),
    # person
    path('api/person/<username>', api.get_person, name='get_person'),
    # person by code
    path('api/person/code/<code>', api.get_person_by_code,
         name='get_person_by_code'),

    # get my messages
    path('api/person/messages/<username>',
         api.get_my_messages, name='get_messages'),

    # get my send messages
    path('api/person/messages/send/<username>',
         api.get_my_send_messages, name='get_my_send_messages'),

    # new message
    path('api/messages/new', api.new_message, name='new_message'),
]
