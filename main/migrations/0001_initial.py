# Generated by Django 5.0.1 on 2024-01-20 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField(help_text='Уникальный идентификатор пользователя в Telegram.', unique=True, verbose_name='ID пользователя')),
                ('image', models.FileField(blank=True, help_text='Изображение пользователя в Telegram.', null=True, upload_to='telegram_user_image', verbose_name='Изображение')),
                ('username', models.CharField(blank=True, help_text='Имя пользователя в Telegram.', max_length=120, null=True, verbose_name='Имя пользователя')),
                ('first_name', models.CharField(blank=True, help_text='Имя пользователя в Telegram.', max_length=120, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, help_text='Фамилия пользователя в Telegram.', max_length=120, null=True, verbose_name='Фамилия')),
                ('language_code', models.CharField(blank=True, help_text='Код языка, используемый пользователем в Telegram.', max_length=10, null=True, verbose_name='Код языка')),
                ('is_bot', models.BooleanField(default=False, help_text='Указывает, является ли пользователь ботом.', verbose_name='Бот')),
                ('admin', models.BooleanField(default=False, help_text='Указывает, является ли пользователь админом.', verbose_name='Админ')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Временная метка, указывающая, когда был создан пользователь.', verbose_name='Создан')),
            ],
            options={
                'verbose_name': 'Пользователь Telegram',
                'verbose_name_plural': 'Пользователи Telegram',
                'ordering': ['-created_at'],
            },
        ),
    ]
