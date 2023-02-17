from django.db import models

# Create your models here.
class Member(models.Model):
    spacename = models.CharField(max_length=256, null=True)
    point = models.IntegerField(default=0)

    class Meta:
        db_table = 'alpha_member'