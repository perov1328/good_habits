from rest_framework.permissions import IsAuthenticated
from habit.models import Habit
from habit.permissions import IsAuthor
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from habit.serializers import HabitSerializer
from habit.paginators import HabitPagination


class HabitCreateAPIView(CreateAPIView):
    """
    Контроллер для создания сущностей модели Привычки
    """
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()


class HabitListAPIView(ListAPIView):
    """
    Контроллер для просмотра списка всех сущностей модели Привычки
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        habits_public = []
        habits = Habit.objects.all()
        for habit in habits:
            if habit.user == self.request.user or habit.is_public:
                habits_public.append(habit)
        return habits_public


class HabitRetriveAPIView(RetrieveAPIView):
    """
    Контроллер для просмотра конкретной сущности модели Привычки
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]


class HabitUpdateAPIView(UpdateAPIView):
    """
    Контроллер для обновления сущности модели Привычки
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsAuthor]


class HabitDeleteAPIView(DestroyAPIView):
    """
    Контроллер для удаления сущности модели Привычки
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsAuthor]
