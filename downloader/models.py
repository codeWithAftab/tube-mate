from django.db import models

# Create your models here.
class History(models.Model):
    search = models.CharField(max_length=400,verbose_name="search history.")
    date = models.DateTimeField(auto_created=True, auto_now=True)

    def __str__(self) -> str:
        return self.search