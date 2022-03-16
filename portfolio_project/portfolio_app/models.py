from django.db import models

# Create your models here.
class contactform(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    content = models.CharField(max_length=1500)

    def __str__(self):
        return self.email
    
    class Mate:
        db_name = ["Contect"]

