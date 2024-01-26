# Generated by Django 5.0.1 on 2024-01-20 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='city',
            field=models.CharField(blank=True, help_text='Город, в котором находится пользователь.', max_length=120, null=True, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='location',
            field=models.CharField(blank=True, help_text='Локация, в которой находится пользователь.', max_length=120, null=True, verbose_name='Локация'),
        ),
    ]
