from django.forms import forms
from .models import contactform

class emailform(contactform):
    form = contactform(forms)
