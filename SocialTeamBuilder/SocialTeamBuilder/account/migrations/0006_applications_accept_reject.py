# Generated by Django 2.2.5 on 2019-10-15 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20191014_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='accept_reject',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]