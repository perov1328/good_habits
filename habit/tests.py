from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from habit.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """
    Тестирование модели Привычки
    """

    def setUp(self):
        """
        Создание тестовой модели Пользователя (с авторизацией) и Привычки
        """
        self.user = User.objects.create(
            email='test@yandex.ru',
            password='test'
        )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            user=self.user,
            place="Street",
            time="21:00",
            action="Run",
            period="3",
            time_to_complete=100
        )

    def test_habit_create(self):
        """
        Тестирование создания Привычки
        """
        data = {
            "user": self.user.pk,
            "place": "Street",
            "time": "22:00",
            "action": "Run",
            "period": "3",
            "time_to_complete": 100
        }
        response = self.client.post(
            reverse('habit:habit_create'),
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            Habit.objects.all().count(),
            2
        )

    def test_habit_list(self):
        """
        Тестирование вывода всех Привычек
        """
        response = self.client.get(reverse('habit:habit_list'))
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_habit_detail(self):
        """
        Тестирование для вывода информации о конкретной привычке
        """
        retrive_url = reverse('habit:habit_detail', args=[self.habit.pk])
        response = self.client.get(retrive_url)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        data = {
            'user': self.user.id,
            'place': 'Street',
            'time': '21:00:00',
            'action': 'Run',
            'good_habit': False,
            'associated_habit': None,
            'period': '3',
            'prize': None,
            'time_to_complete': 100,
            'is_public': False
        }
        resived_data = response.json()
        resived_data.pop('id')
        self.assertEqual(
            resived_data,
            data
        )

    def test_habit_delete(self):
        """
        Тестирование для удаления Привычки
        """
        delete_url = reverse('habit:habit_delete', args=[self.habit.pk])
        response = self.client.delete(delete_url)
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Habit.objects.filter(id=self.habit.pk).count(),
            0
        )

    def test_habit_update(self):
        """
        Тестирование для обновления информации по Привычке
        """
        update_url = reverse('habit:habit_update', args=[self.habit.pk])
        update_data = {
            'place': 'Job',
            'time_to_complete': 120
        }
        response = self.client.patch(update_url, update_data, format='json')
        self.habit.refresh_from_db()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(self.habit.place, update_data['place'])
        self.assertEqual(self.habit.time_to_complete, update_data['time_to_complete'])
