from rest_framework.serializers import ValidationError


class TimeToCompleteValidator:
    """
    Валидатор для указания времени необходимого на выполнение привычки
    """
    def __init__(self, time_to_complete):
        self.time_to_complete = time_to_complete

    def __call__(self, value):
        time = value.get(self.time_to_complete)
        if int(time) > 120:
            raise ValidationError('Время на выполнение привычки не должно превышать 2х минут (120 секунд).')


class AssociatedAndPrizeValidator:
    """
    Валидатор для исключения одновременного выбора связанной привычки и вознаграждения
    """
    def __init__(self, associated_habit, prize):
        self.associated_habit = associated_habit
        self.prize = prize

    def __call__(self, value):
        associated = value.get(self.associated_habit)
        prize = value.get(self.prize)
        if not associated and prize:
            raise ValidationError('Нельзя одновременно выбрать связанную привычку и вознаграждение.')


class AssociatedValidator:
    """
    Валидатор для проверки, является ли связанная привычка приятной
    """
    def __init__(self, associated_habit, good_habit):
        self.associated_habit = associated_habit
        self.good_habit = good_habit

    def __call__(self, value):
        associated = value.get(self.associated_habit)
        good_habit = value.get(self.good_habit)
        if associated and not good_habit:
            raise ValidationError('В связанные привычки могут попадать только привычки с приятным признаком.')


class GoodHabitValidator:
    """
    Валидатор что у приятной привычки не может быть вознаграждения или связанной привычки
    """
    def __init__(self, good_habit, associated_habit, prize):
        self.good_habit = good_habit
        self.associated_habit = associated_habit
        self.prize = prize

    def __call__(self, value):
        good_habit = value.get(self.good_habit)
        associated = value.get(self.associated_habit)
        prize = value.get(self.prize)
        if not good_habit and (associated or prize):
            raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки.')
