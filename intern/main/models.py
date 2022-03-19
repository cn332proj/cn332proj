from django.db import models
from django.utils import timezone

# Create your models here.
class News(models.Model):
    header = models.CharField(max_length=150, null = True,)
    pdf = models.FileField(blank=True,null=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.header