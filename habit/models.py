from django.db import models
from users.models import User
from prize.models import Prize
from habit.constants import HABIT_PLACE, HABIT_PERIOD, NULLABLE


class Habit(models.Model):
    """
    Модель привычки
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', null=True)
    place = models.CharField(max_length=10, choices=HABIT_PLACE, verbose_name='Место')
    time = models.TimeField(verbose_name='Время')
    action = models.CharField(max_length=100, verbose_name='Действие')
    good_habit = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    associated_habit = models.ForeignKey('self', on_delete=models.CASCADE,
                                         **NULLABLE, verbose_name='Связанная привычка')
    period = models.CharField(max_length=20, choices=HABIT_PERIOD, verbose_name='Периодичность')
    prize = models.FloatField(Prize, **NULLABLE)
    time_to_complete = models.IntegerField(verbose_name='Время на выполнение')
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')
    date_of_creation = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        """
        Возвращение строкового представления объекта
        """
        return f'{self.user} будет {self.action} {self.time} на {self.place}'

    class Meta:
        """
        Настройки для наименования объекта/объектов
        """
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ('user', 'action', 'date_of_creation',)
