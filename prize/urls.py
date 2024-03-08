from prize.apiviews import (PrizeCreateAPIView, PrizeListAPIView, PrizeDeleteAPIView,
                            PrizeUpdateAPIView, PrizeRetrieveAPIView)
from prize.apps import PrizeConfig
from django.urls import path

app_name = PrizeConfig.name

urlpatterns = [
    path('', PrizeListAPIView.as_view(), name='prize_list'),
    path('create/', PrizeCreateAPIView.as_view(), name='prize_create'),
    path('<int:pk>/', PrizeRetrieveAPIView.as_view(), name='prize_detail'),
    path('delete/<int:pk>/', PrizeDeleteAPIView.as_view(), name='prize_delete'),
    path('update/<int:pk>/', PrizeUpdateAPIView.as_view(), name='prize_update')
]
