from django.db import models

# Create your models here.
class Character(models.Model):
    max_point = models.IntegerField()
    image = models.CharField(max_length=128)
    max_origin = models.IntegerField()
    
    class Meta:
        db_table = 'alpha_character'