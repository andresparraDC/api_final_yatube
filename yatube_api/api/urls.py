""" Српинт 9: Проект «API для Yatube»
Автор: Фредди Андрес Парра Орельяна
Студент факультета Бэкенд. Когорта 14+

Файл urls.py
Основная функция: определение URL-адресов проекта

Router -> регистрация PostViewSet, GroupViewSet и CommentViewSet
urlpatterns -> url-адреса проекта: api и как получить токен автоматически.

"""
from django.urls import include
from django.urls import path

from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

from .views import CommentViewSet
from .views import FollowViewSet
from .views import GroupViewSet
from .views import PostViewSet


v1_router = DefaultRouter()
v1_router.register(
    'groups',
    GroupViewSet,
    basename='groups'
)
v1_router.register(
    'posts',
    PostViewSet,
    basename='posts'
)
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
v1_router.register(
    'follow',
    FollowViewSet,
    basename='follow'
)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/token/', TokenObtainPairView.as_view()),
    path('v1/token/refresh', TokenRefreshView.as_view())
]
