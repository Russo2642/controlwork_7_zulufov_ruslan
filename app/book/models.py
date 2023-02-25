from django.db import models


# Create your models here.
class StatusChoice(models.TextChoices):
    ACTIVE = 'ACTIVE', 'Активно'
    BLOCKED = 'BLOCKED', 'Заблокировано'


class Book(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name="Имя")
    email = models.EmailField(max_length=300, null=False, blank=False, verbose_name="Почта")
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Текст")
    status = models.CharField(max_length=50, null=False, blank=False, verbose_name="Статус",
                              choices=StatusChoice.choices, default=StatusChoice.BLOCKED)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")

    def __str__(self):
        return f"{self.name} - {self.email} - {self.created_at}"

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-created_at']
