from rest_framework.pagination import PageNumberPagination


class PrizePagination(PageNumberPagination):
    """
    Пагинатор для вывода списка вознаграждений
    """
    page_size = 5
