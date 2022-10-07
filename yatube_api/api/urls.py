""" Српинт 9: Проект «API для Yatube»
Автор: Фредди Андрес Парра Орельяна
Студент факультета Бэкенд. Когорта 14+

Файл urls.py
Основная функция: определение URL-адресов проекта

Router -> регистрация PostViewSet, GroupViewSet и CommentViewSet
urlpatterns -> url-адреса проекта: api и как получить токен автоматически.

"""
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet


version = 'v1'
app_name = 'posts'

router = DefaultRouter()
router.register(
    'groups',
    GroupViewSet,
    basename='groups'
)
router.register(
    'posts',
    PostViewSet,
    basename='posts'
)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register(
    'follow',
    FollowViewSet,
    basename='follow'
)

urlpatterns = [
    path(f'{version}/', include(router.urls)),
    path(f'{version}/auth/', include('djoser.urls')),
    path(f'{version}/', include('djoser.urls.jwt')),
    path(f'{version}/token/', TokenObtainPairView.as_view()),
    path(f'{version}/token/refresh', TokenRefreshView.as_view())
]
