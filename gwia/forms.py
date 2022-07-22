from dataclasses import fields
from django import forms
from .models import PersonMessage


class MessageForm(forms.ModelForm):
    class Meta:
        model = PersonMessage
        fields = ['message']
