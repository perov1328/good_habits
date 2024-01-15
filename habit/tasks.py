from datetime import datetime
from celery import shared_task
from habit.models import Habit
from habit.services import TGBot


@shared_task
def task_send_message():
    date_now = datetime.today().weekday()
    time_now = datetime.utcnow().time().strftime('%H:%M')

    habits = Habit.objects.filter(good_habit=False)

    for habit in habits:
        if habit.time.strftime('%H:%M') == time_now and habit.period <= date_now:
            chat_id = habit.user.tg_id
            text_message = (f"Дружище, пора {habit.action} на {habit.place}"
                            f"Ты сам захотел это делать на {habit.place}"
                            f"И давай не откладывай, на это нужно всего лишь {habit.time_to_complete} секунд")
            if habit.prize:
                text_message += f"\nА в подарок можешь позволнить себе {habit.prize.title}"
            message = TGBot()
            message.send_habit(text=text_message, chat_id=chat_id)
