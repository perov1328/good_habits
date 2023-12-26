from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from prize.models import Prize
from users.models import User


class PrizeTestCase(APITestCase):
    """
    Тестирование модели Вознаграждения
    """

    def setUp(self):
        """
        Создание тестовое модели Пользователя (с авторизацией) и Вознаграждения
        """
        self.user = User.objects.create(
            email='test@yandex.ru',
            password='test'
        )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.prize = Prize.objects.create(
            title="test 1",
            description="test 1",
            user=self.user
        )

    def test_prize_create(self):
        """
        Тестирование создания Вознаграждения
        """
        data = {
            "title": "test 2",
            "description": "test 2",
            "user": self.user.pk
        }
        response = self.client.post(
            reverse('prize:prize_create'),
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            Prize.objects.all().count(),
            2
        )

    def test_prize_list(self):
        """
        Тестирование вывода всех Вознаграждений
        """
        response = self.client.get(reverse('prize:prize_list'))
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_prize_detail(self):
        """
        Тестирование для вывода информации о конкретном Вознаграждении
        """
        retrive_url = reverse('prize:prize_detail', args=[self.prize.pk])
        response = self.client.get(retrive_url)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        data = {
            "title": "test 1",
            "description": "test 1",
            "user": self.user.pk
        }
        resived_data = response.json()
        resived_data.pop('id')
        self.assertEqual(
            resived_data,
            data
        )

    def test_prize_delete(self):
        """
        Тестирование для удаления Вознаграждения
        """
        delete_url = reverse('prize:prize_delete', args=[self.prize.pk])
        response = self.client.delete(delete_url)
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(Prize.objects.filter(id=self.prize.pk).count(), 0)

    def test_prize_update(self):
        """
        Тестирование для обновления информации по Вознаграждению
        """
        update_url = reverse('prize:prize_update', args=[self.prize.pk])
        update_data = {
            "title": "test",
            "description": "test"
        }
        response = self.client.patch(update_url, update_data, format='json')
        self.prize.refresh_from_db()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(self.prize.title, update_data["title"])
        self.assertEqual(self.prize.description, update_data["description"])
