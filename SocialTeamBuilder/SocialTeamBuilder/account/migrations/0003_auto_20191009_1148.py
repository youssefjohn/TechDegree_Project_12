# Generated by Django 2.2.5 on 2019-10-09 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20191008_1231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='position',
        ),
        migrations.AddField(
            model_name='project',
            name='position',
            field=models.ManyToManyField(blank=True, default=None, to='account.PositionModel'),
        ),
    ]
