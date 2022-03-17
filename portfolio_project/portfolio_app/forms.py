from .models import contactform
from django.forms import ModelForm,TextInput,Textarea,EmailInput

class emailform(ModelForm):
    class Meta():
        model = contactform
        fields = '__all__'
        Widgets = {
            'username': TextInput(attrs={'class':'form-control','placeholder':'type your name'}),
            'email': EmailInput(attrs={'class':'form-control','placeholder':'type your name'}),
            'Description': Textarea(attrs={'col':80,'row':50}),

        }
