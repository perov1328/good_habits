from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    """
    Контроллер для создания сущности моедли Пользователя
    """
    serializer_class = UserSerializer


class UserRetrieveAPIView(RetrieveAPIView):
    """
    Контроллер для просмотора конкретной сущности модели Пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPIView(UpdateAPIView):
    """
    Контроллер для обновления сущности модели Пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDeleteAPIView(DestroyAPIView):
    """
    Контроллер для удаления сущности модели Пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
