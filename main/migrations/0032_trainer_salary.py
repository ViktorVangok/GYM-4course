# Generated by Django 3.2 on 2021-08-20 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_trainerachivement'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='salary',
            field=models.IntegerField(default=0),
        ),
    ]
