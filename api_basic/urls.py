from django.urls import path, include

from .api import ArticleViewSet
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('', ArticleViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.home, name='article-home'),


]
