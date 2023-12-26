from rest_framework import serializers
from prize.models import Prize


class PrizeSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Вознаграждения
    """

    class Meta:
        model = Prize
        fields = ('id', 'title', 'description', 'user',)
