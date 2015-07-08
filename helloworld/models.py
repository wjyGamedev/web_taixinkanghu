from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Account(models.Model):
    url = models.IntegerField(unique=True)