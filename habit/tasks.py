from celery import shared_task
from habit.services import get_tg_update, get_scheduler


@shared_task
def habit_time():
    """
    Проверка времени и отправка сообщения пользователю
    """
    get_tg_update()
    get_scheduler()
