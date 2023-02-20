from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Member(AbstractUser):
    spacename = models.CharField(max_length=256, null=True)
    point = models.IntegerField(default=0)

    class Meta:
        db_table = 'alpha_member'

class Log(models.Model):
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE)
    mission = models.ForeignKey('mission.Mission', on_delete=models.CASCADE)
    status = models.CharField(max_length=32, default='ready',
        choices=(
            ('ready', 'ready'),
            ('clicked', 'clicked'),
            ('done', 'done')
        ),
    )
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'alpha_log'