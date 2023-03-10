from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Member(AbstractUser):
    spacename = models.CharField(max_length=256, null=True)
    point = models.IntegerField(default=0)

    class Meta:
        db_table = 'alpha_member'

class Coupon(models.Model):
    detail = models.CharField(max_length=256)
    image = models.CharField(max_length=128)

    class Meta:
        db_table = 'alpha_coupon'