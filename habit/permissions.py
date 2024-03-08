from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):
    """
    Права доступа для создателя привычки
    """
    message = 'Вы не являетесь автором данной привычки.'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False
