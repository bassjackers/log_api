from django.db import router
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'get', views.LogDataViewSet)
router.register(r'post', views.LogDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
