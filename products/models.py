from django.db import models
from datetime import datetime
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to ='photo/%Y/%m/%d/', blank =True, null=True)
    published_at = models.DateTimeField(default = datetime.now)

    def __str__(self):
        return self.name

  