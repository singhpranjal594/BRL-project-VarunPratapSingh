# Generated by Django 3.0.7 on 2020-09-03 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='phone',
            field=models.CharField(default=0, max_length=12),
        ),
        migrations.AlterField(
            model_name='information',
            name='roll_no',
            field=models.CharField(default=0, max_length=15, unique=True),
        ),
    ]
