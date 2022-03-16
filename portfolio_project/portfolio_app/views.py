from django.shortcuts import render
from django.http import HttpResponse
from .forms import emailform
from .models import contactform

# Create your views here.

def index(request):
    form = emailform.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    contaxt = {'forms':form}

    return render(request,'index.html',contaxt)