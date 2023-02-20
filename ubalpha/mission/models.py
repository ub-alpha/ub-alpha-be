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

class Log(models.Model):
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE)
    mission = models.ForeignKey('mission.Mission', on_delete=models.CASCADE)
    status = models.CharField(max_length=32, default='ready',
        choices=(
            ('ready', 'ready'),
            ('done', 'done')
        ),
    )
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'alpha_log'