from django.forms import ModelForm
from service.models import Contact


class MessageForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']