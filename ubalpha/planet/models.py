from django.db import models

# Create your models here.
class Planet(models.Model):
    image = models.CharField(max_length=128)

    class Meta:
        db_table = 'alpha_planet'