from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import emailform
from .models import contactform

# Create your views here.

def index(request):
    forms = emailform(request.POST)
    if request.method == 'POST':
        if forms.is_valid():
            forms.save()
    else:
        forms = emailform()
    contaxt = {'forms':forms}

    return render(request,'index.html',contaxt)