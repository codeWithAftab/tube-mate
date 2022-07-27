import email
from django.db import models

# Create your models here.
class History(models.Model):
    search = models.CharField(max_length=400,verbose_name="search history.")
    date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.search

class classImages(models.Model):
    name=models.CharField(max_length=122)
    enrol_no = models.IntegerField(verbose_name="Enrollment no")
    image_url = models.CharField(max_length=12333,default="")
    prog = models.CharField(max_length=30)
    email = models.EmailField(default="")
    def __str__(self) -> str:
        return self.name