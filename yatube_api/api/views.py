""" Српинт 9: Проект «API для Yatube»
Автор: Фредди Андрес Парра Орельяна
Студент факультета Бэкенд. Когорта 14+

Файл views.py

"""
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from posts.models import Group, Post, User
from rest_framework import filters, mixins, permissions, status, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .permisions import IsAuthorOrGuest
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    """Класс связан с моделью Post.
    Можно ли создавать сообщения из API."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAuthorOrGuest,
    ]
    pagination_class = LimitOffsetPagination
    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_fields = (
        'group',
    )

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
        IsAuthorOrGuest,
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


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Класс связан с моделью Group.
    Можно ли создавать сообщения из API."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [
        IsAuthorOrGuest,
    ]

    def create(self, request):
        return Response(
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )


class FollowViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Класс связан с моделью Follow.
    Можно ли создавать сообщения из API."""

    http_method_names = [
        'get',
        'post',
    ]
    serializer_class = FollowSerializer
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    search_fields = [
        'user__username',
        'following__username'
    ]
    permission_classes = [
        permissions.IsAuthenticated,
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
