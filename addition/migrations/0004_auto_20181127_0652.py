# Generated by Django 2.1.3 on 2018-11-27 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addition', '0003_auto_20181127_0634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addition',
            name='add',
        ),
        migrations.AddField(
            model_name='addition',
            name='operation',
            field=models.CharField(default=0, max_length=1),
        ),
    ]
