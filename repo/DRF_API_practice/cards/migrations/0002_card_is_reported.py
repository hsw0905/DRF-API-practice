# Generated by Django 3.0.7 on 2020-06-14 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='is_reported',
            field=models.BooleanField(default=False),
        ),
    ]
