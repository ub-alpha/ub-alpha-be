# Generated by Django 4.1.7 on 2023-02-20 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_delete_log'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(max_length=256)),
                ('image', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'alpha_coupon',
            },
        ),
    ]
