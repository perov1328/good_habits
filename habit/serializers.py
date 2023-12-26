from rest_framework import serializers
from habit.models import Habit
from habit.validators import (TimeToCompleteValidator, AssociatedAndPrizeValidator,
                              AssociatedValidator, GoodHabitValidator)


class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Привычек
    """

    class Meta:
        model = Habit
        fields = ('id', 'user', 'place', 'time', 'action', 'good_habit', 'associated_habit',
                  'period', 'prize', 'time_to_complete', 'is_public',)
        validators = [
            TimeToCompleteValidator(time_to_complete='time_to_complete'),
            AssociatedAndPrizeValidator(associated_habit='associated_habit', prize='prize'),
            AssociatedValidator(associated_habit='associated_habit', good_habit='good_habit'),
            GoodHabitValidator(good_habit='good_habit', associated_habit='associated_habit', prize='prize')
        ]
