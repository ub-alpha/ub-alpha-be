from django.db import models

# Create your models here.
class Mission(models.Model):
    point = models.IntegerField()
    category = models.CharField(max_length=128,
        choices=(
            ('daily', 'daily'),
            ('welcome', 'welcome'),
        )
    )
    mission = models.CharField(max_length=512)

    class Meta:
        db_table = 'alpha_mission'