from django.contrib import admin
from .models import Person, PersonMessage
from django.contrib.auth.models import Group, User


admin.site.register(Person)
admin.site.register(PersonMessage)

admin.site.unregister(Group)
admin.site.unregister(User)
