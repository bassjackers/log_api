from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import LogDataViewSet

logdata_list = LogDataViewSet.as_view({'get': 'list'})
logdata_detail = LogDataViewSet.as_view({'get': 'retrieve'})


# router = DefaultRouter()
# router.register(r'', views.LogDataViewSet)

urlpatterns = [
    path('datas', logdata_list, name='logdata-list'),
    path('datas/<int:pk>', logdata_detail, name='logdata-list')
]
