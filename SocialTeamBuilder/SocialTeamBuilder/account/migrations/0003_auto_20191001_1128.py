# Generated by Django 2.2.5 on 2019-10-01 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20191001_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='bio',
            field=models.TextField(blank=True),
        ),
    ]
