from django.db import models

# Create your models here.
class Planet(models.Model):
    image = models.CharField(max_length=128)

    class Meta:
        db_table = 'alpha_planet'


class Detail(models.Model):
    member = models.ForeignKey('member.Member', on_delete=models.CASCADE)
    planet = models.ForeignKey('planet.Planet', on_delete=models.CASCADE)
    character = models.ForeignKey('character.Character', on_delete=models.CASCADE)
    status = models.CharField(max_length=128, default='unused',
        choices=(
            ('unused', 'unused'),
            ('used', 'used'),
        ),
    )
    point = models.IntegerField(default=0)

    class Meta:
        db_table = 'detail'