import requests
from django.core.exceptions import ObjectDoesNotExist
from habit.models import Habit
from datetime import datetime
from collections import defaultdict
from config.settings import TELEGRAM_URL, TELEGRAM_TOKEN
from users.models import User


def send_tg_message(message):
    """
    Функция для отправки сообщения пользователю в ТГ
    """
    url = f'{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage'
    for chat_id, message in message.items():
        params = {'chat_id': chat_id, 'text': message}
        requests.get(url, params=params)


def check_habit(habit, time_now):
    """
    Функция для проверки привычки и добавлении её в сообщение
    """
    if habit.period <= 7:
        if habit.time.strftime('%H:%M') == time_now.strftime('%H:%M'):
            chat_id = habit.user.tg_id
            message = f'{habit.action} на {habit.place}\n'
            if habit.prize:
                message += f'в награду можно - {habit.prize}\n'
            elif habit.associated_habit:
                message += f'в награду можно - {habit.associated_habit}\n'
            else:
                message += 'И ты будешь чуть больше чем крутой!\n'
            message += f'Дел то всего на {habit.time_to_complete} секунд!'
            return chat_id, message
    return None, None


def get_group_habits(habits):
    """
    Функция для группирования привычек по дню и времени
    """
    group_habits = defaultdict(list)
    for habit in habits:
        group_habits[(habit.time, habit.place)].append(habit)
    return group_habits


def combinaed_message(grouped_habits, time_now, date_now):
    """
    Функция для создания объединенного сообщения на основе групп привычек
    """
    combined_message = ''
    chat_ids = []
    for habit in grouped_habits:
        chat_id, message = check_habit(habit, time_now)
        if chat_id and message:
            chat_ids.append(chat_id)
            combined_message += message + '\n\n\n'
    return chat_ids, combined_message


def get_scheduler():
    """
    Функция для проверки времени/дня выполнения привычек и отправке сообщения в ТГ
    """
    time_now = datetime.now()
    date_now = datetime.today().weekday()
    habits = Habit.objects.filter(good_habit=False, period__lte=date_now)
    group_habits = get_group_habits(habits)
    messages = {}
    for (time, period), grouped_habits in group_habits.items():
        tg_ids, combined_message = combinaed_message(grouped_habits, time_now, date_now)
        if tg_ids and combined_message:
            for tg_id in tg_ids:
                messages[tg_id] = combined_message
    send_tg_message(messages)


def get_tg_update():
    """
    Получение информации от ТГ бота
    """
    url = f'{TELEGRAM_URL}{TELEGRAM_TOKEN}/getUpdates'
    response = requests.get(url)
    if response.status_code == 200:
        for telegram_users in response.json()["result"]:
            tg_user_id = telegram_users["message"]["from"]["id"]
            tg_name = telegram_users["message"]["from"]["username"]
            try:
                user = User.objects.get(tg_name=tg_name)
                if user.chat_id is None:
                    user.chat_id = tg_user_id
                    user.save()
            except ObjectDoesNotExist:
                print("Пользователь не найден в базе данных.")
