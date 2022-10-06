""" Српинт 9: Проект «API для Yatube»
Автор: Фредди Андрес Парра Орельяна
Студент факультета Бэкенд. Когорта 14+

Файл views.py

"""
from django.shortcuts import get_object_or_404

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import permissions
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Group
from posts.models import Post
from posts.models import User

from .permisions import IsAuthorOrGuest
from .permisions import ReadOnly
from .serializers import CommentSerializer
from .serializers import FollowSerializer
from .serializers import GroupSerializer
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Класс связан с моделью Post.
    Можно ли создавать сообщения из API."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAuthorOrGuest
    ]
    pagination_class = LimitOffsetPagination
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_fields = ('group',)

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user
        )


class CommentViewSet(viewsets.ModelViewSet):
    """Класс связан с моделью Comment.
    Можно ли создавать сообщения из API."""

    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAuthorOrGuest
    ]

    def perform_create(self, serializer):
        post = get_object_or_404(
            Post,
            pk=self.kwargs.get('post_id')
        )
        serializer.save(
            author=self.request.user,
            post=post
        )

    def get_queryset(self):
        post = get_object_or_404(
            Post,
            pk=self.kwargs.get('post_id')
        )
        return post.comments.all()

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()


class GroupViewSet(viewsets.ModelViewSet):
    """Класс связан с моделью Group.
    Можно ли создавать сообщения из API."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [
        IsAuthorOrGuest
    ]

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()

    def create(self, request):
        return Response(
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def group_pk(self, request):
        group = get_object_or_404(
            Group,
            pk=self.kwargs.get('group_id')
        )
        return group


class FollowViewSet(viewsets.ModelViewSet):
    """Класс связан с моделью Follow.
    Можно ли создавать сообщения из API."""

    serializer_class = FollowSerializer
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend
    ]
    search_fields = [
        'user__username',
        'following__username'
    ]
    http_method_names = [
        'get',
        'post'
    ]
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        user = get_object_or_404(
            User,
            username=self.request.user.username
        )
        return user.follower.all()

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )
