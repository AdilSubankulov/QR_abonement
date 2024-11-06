from django.urls import path
from .views import TariffViewSet, UserProfileViewSet, UserAbonementViewSet

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

    path('user-profiles/', UserProfileViewSet.as_view(
        {'get': 'list',
         'post': 'create'
         }), name='user-profile-list'),
    path('user-profiles/<int:pk>/', UserProfileViewSet.as_view(
        {'get': 'retrieve',
         'put': 'update',
         'delete': 'destroy'
         }), name='user-profile-detail'),

    path('user-abonements/', UserAbonementViewSet.as_view(
        {'get': 'list',
         'post': 'create'
         }), name='user-abonement-list'),
    path('user-abonements/<int:pk>/', UserAbonementViewSet.as_view(
        {'get': 'retrieve',
         'put': 'update',
         'delete': 'destroy'
         }), name='user-abonement-detail'),
]

