from rest_framework.permissions import IsAuthenticated
from prize.models import Prize
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from prize.paginators import PrizePagination
from prize.serializers import PrizeSerializer


class PrizeCreateAPIView(CreateAPIView):
    """
    Контролер для создания сущности модели Вознаграждения
    """
    serializer_class = PrizeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()


class PrizeListAPIView(ListAPIView):
    """
    Контроллер для просмотра списка всех сущностей модели Вознаграждения
    """
    queryset = Prize.objects.all()
    serializer_class = PrizeSerializer
    pagination_class = PrizePagination
    permission_classes = [IsAuthenticated]


class PrizeRetrieveAPIView(RetrieveAPIView):
    """
    Контроллер для просмотра конкретной сущности модели Вознаграждения
    """
    queryset = Prize.objects.all()
    serializer_class = PrizeSerializer
    permission_classes = [IsAuthenticated]


class PrizeUpdateAPIView(UpdateAPIView):
    """
    Контроллер для обновления сущности модели Вознаграждения
    """
    queryset = Prize.objects.all()
    serializer_class = PrizeSerializer
    permission_classes = [IsAuthenticated]


class PrizeDeleteAPIView(DestroyAPIView):
    """
    Контроллер для удаления сущности модели Вознаграждения
    """
    queryset = Prize.objects.all()
    serializer_class = PrizeSerializer
    permission_classes = [IsAuthenticated]
