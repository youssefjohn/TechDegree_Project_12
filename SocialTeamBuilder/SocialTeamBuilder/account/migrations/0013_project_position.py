# Generated by Django 2.2.5 on 2019-10-07 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_remove_project_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='position',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.PositionModel'),
        ),
    ]