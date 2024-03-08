from habit.apps import HabitConfig
from django.urls import path
from habit.apiviews import (HabitListAPIView, HabitCreateAPIView, HabitUpdateAPIView,
                            HabitRetriveAPIView, HabitDeleteAPIView)

app_name = HabitConfig.name

urlpatterns = [
    path('', HabitListAPIView.as_view(), name='habit_list'),
    path('create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('<int:pk>/', HabitRetriveAPIView.as_view(), name='habit_detail'),
    path('delete/<int:pk>/', HabitDeleteAPIView.as_view(), name='habit_delete'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
]
