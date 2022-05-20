from django.db import models

# Create your models here.
class urls(models.Model):
    url =models.TextField()

    def __str__(self) -> str:
        return self.url