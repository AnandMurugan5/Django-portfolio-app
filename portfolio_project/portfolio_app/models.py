from django.db import models

# Create your models here.
class contactform(models.Model):
    Name = models.CharField(max_length=50)
    email = models.EmailField()
    Description = models.CharField(max_length=1500)

    def __str__(self):
        return self.Name
    
    class Mate:
        db_name = "Contect"

