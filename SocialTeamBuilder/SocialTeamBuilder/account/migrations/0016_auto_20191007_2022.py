# Generated by Django 2.2.5 on 2019-10-07 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_auto_20191007_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='position',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.PositionModel'),
        ),
    ]
