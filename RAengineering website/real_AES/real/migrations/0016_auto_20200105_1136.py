# Generated by Django 3.0 on 2020-01-05 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0015_auto_20200105_1102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='nam_c',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=70),
        ),
    ]
