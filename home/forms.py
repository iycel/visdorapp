from django import forms
from .models import Contact
from django.forms.widgets import TextInput

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone_number', 'email', 'message']
        # fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder' : 'Name'}),
            'email' : forms.EmailInput(attrs={'placeholder' : 'Email'}),
            'phone_number' : forms.TextInput(attrs={'placeholder' : 'Phone'}),
            'message' : forms.TextInput(attrs={'placeholder' : 'Message'})
        }