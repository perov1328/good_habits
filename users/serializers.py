from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Пользователя
    """
    class Meta:
        model = User
        fields = ('id', 'email', 'tg_name', 'tg_id', 'password',)
