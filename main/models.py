from django.db import models


class TelegramUser(models.Model):
    user_id = models.BigIntegerField(
        unique=True,
        verbose_name="ID пользователя",
        help_text="Уникальный идентификатор пользователя в Telegram.",
    )
    image = models.FileField(
        upload_to="telegram_user_image",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Изображение пользователя в Telegram.",
    )
    username = models.CharField(
        max_length=120,
        blank=True,
        null=True,
        verbose_name="Имя пользователя",
        help_text="Имя пользователя в Telegram.",
    )
    first_name = models.CharField(
        max_length=120,
        blank=True,
        null=True,
        verbose_name="Имя",
        help_text="Имя пользователя в Telegram.",
    )
    last_name = models.CharField(
        max_length=120,
        blank=True,
        null=True,
        verbose_name="Фамилия",
        help_text="Фамилия пользователя в Telegram.",
    )
    language_code = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name="Код языка",
        help_text="Код языка, используемый пользователем в Telegram.",
    )
    is_bot = models.BooleanField(
        default=False,
        verbose_name="Бот",
        help_text="Указывает, является ли пользователь ботом.",
    )
    admin = models.BooleanField(
        default=False,
        verbose_name="Админ",
        help_text="Указывает, является ли пользователь админом.",
    )
    city = models.CharField(
        verbose_name="Город",
        max_length=120,
        blank=True,
        null=True,
        help_text="Город, в котором находится пользователь.",
    )
    location = models.CharField(
        verbose_name="Локация",
        max_length=120,
        blank=True,
        null=True,
        help_text="Локация, в которой находится пользователь.",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Создан",
        help_text="Временная метка, указывающая, когда был создан пользователь.",
    )

    def get_name(self):
        if self.username:
            return self.username
        elif self.last_name:
            return self.last_name
        elif self.first_name:
            return self.first_name
        else:
            return "Пользователь"
        
    def get_full_name(self):
        if self.last_name and self.first_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return "Пользователь"

    def __str__(self):
        return f"{self.user_id}: {self.get_name()}"

    class Meta:
        verbose_name = "Пользователь Telegram"
        verbose_name_plural = "Пользователи Telegram"
        ordering = ["-created_at"]


class TelegramAds(models.Model):
    image = models.ImageField(
        upload_to="telegram_ads_image",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Изображение рекламы.",
    )
    text = models.TextField(
        blank=True,
        null=True,
        verbose_name="Текст",
        help_text="Текст рекламы.",
    )
    url = models.URLField(
        blank=True,
        null=True,
        verbose_name="Ссылка",
        help_text="Ссылка на рекламе.",
    )
    url2 = models.URLField(
        blank=True,
        null=True,
        verbose_name="Ссылка",
        help_text="Ссылка 2 на рекламе.",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Создан",
        help_text="Временная метка, указывающая, когда была создана реклама.",
    )

    def __str__(self) -> str:
        return f"{self.id}: {self.text[:20]}..."
    
    class Meta:
        verbose_name = "Реклама Telegram"
        verbose_name_plural = "Рекламы Telegram"
        ordering = ["-created_at"]