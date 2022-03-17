from .models import contactform
from django.forms import ModelForm,TextInput,Textarea,EmailInput

class emailform(ModelForm):
    class Meta():
        model = contactform
        fields = '__all__'
        Widgets = {
            'Name': TextInput(attrs={'class':'form-control','placeholder':'type your name'}),
            'Email_ID': EmailInput(attrs={'class':'form-control','placeholder':'type your name'}),
            'Description': Textarea(attrs={'col':80,'row':50}),

        }
