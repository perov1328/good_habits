from django.db import models
from users.models import User


class Prize(models.Model):
    """
    Модель вознаграждения
    """
    title = models.CharField(max_length=100, verbose_name='Наименование вознаграждения')
    description = models.TextField(verbose_name='Описание награды')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', null=True)

    def __str__(self):
        """
        Возвращение строкового представления объекта
        """
        return self.title

    class Meta:
        """
        Настройки для наименования объекта/объектов
        """
        verbose_name = 'Вознаграждение'
        verbose_name_plural = 'Вознаграждения'
