# Generated by Django 4.1.3 on 2023-02-22 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1992-06-13'),
            preserve_default=False,
        ),
    ]
