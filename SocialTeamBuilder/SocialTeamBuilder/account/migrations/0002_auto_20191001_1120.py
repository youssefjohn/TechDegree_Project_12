# Generated by Django 2.2.5 on 2019-10-01 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_pictures'),
        ),
    ]
