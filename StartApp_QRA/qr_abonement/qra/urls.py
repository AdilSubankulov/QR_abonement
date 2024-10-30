from django.urls import path
from .views import TariffViewSet

urlpatterns = [
    path('tariff/', TariffViewSet.as_view(
        {
            'get': 'list',
            'post': 'create'
        }), name='tariff-list'),  # Список и создание тарифов

    path('tariff/<int:pk>/', TariffViewSet.as_view(
        {'get': 'retrieve',
         'put': 'update',
         'delete': 'destroy'
         }), name='tariff-detail'),  # Получение, обновление и удаление конкретного тарифа
]