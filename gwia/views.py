from django.shortcuts import get_object_or_404, render

from gwia.models import Person, PersonMessage
from .forms import MessageForm


def index(request):
    return render(request, template_name='index.html')


def send_message(request, username):
    user = get_object_or_404(Person, username__exact=username)

    if request.method == "GET":
        form = MessageForm()
        return render(request, template_name='send_message.html', context={"form": form})

    if request.method == "POST":

        form = MessageForm(request.POST)

        if form.is_valid():

            personMessage = PersonMessage()
            personMessage.sender_username = "anonymous"
            personMessage.receiver_username = username
            personMessage.sender_code = "anonymous"
            personMessage.receiver_code = user.code
            personMessage.image = form.data.get("image")
            personMessage.message = form.data.get("message")
            personMessage.save()

            return render(request, template_name='sent.html')

        return render(request, template_name='send_message.html', context={"form": form})
