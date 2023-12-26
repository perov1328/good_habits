from rest_framework.pagination import PageNumberPagination


class HabitPagination(PageNumberPagination):
    """
    Пагинатор для вывода списка Привычек
    """
    page_size = 5
