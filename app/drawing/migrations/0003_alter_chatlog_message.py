# Generated by Django 3.2.11 on 2022-01-18 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drawing', '0002_auto_20220118_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatlog',
            name='message',
            field=models.CharField(max_length=255, verbose_name='message'),
        ),
    ]
