# Generated by Django 3.0 on 2020-01-04 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=70),
        ),
    ]