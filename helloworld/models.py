from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Account(models.Model):
    mobile_phone_num = models.IntegerField(unique=True)