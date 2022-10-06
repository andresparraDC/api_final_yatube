""" Српинт 9: Проект «API для Yatube»
Автор: Фредди Андрес Парра Орельяна
Студент факультета Бэкенд. Когорта 14+

Файл serializers.py
Основная функция: получившийся Python-словарь конвертируется
(«рендерится») в JSON.
"""
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment
from posts.models import Follow
from posts.models import Group
from posts.models import Post
from posts.models import User


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор, работающий с моделью Group
    (унаследованной от ModelSerializer)."""

    class Meta:
        """Мета-класс определяет модель,
        с которой вы работаете, и используемые поля."""
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор, работающий с моделью Post
    (унаследованной от ModelSerializer)."""

    author = SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        """Мета-класс определяет модель,
        с которой вы работаете, и используемые поля."""
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор, работающий с моделью Comment
    (унаследованной от ModelSerializer)."""

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        """Мета-класс определяет модель,
        с которой вы работаете, и используемые поля."""
        model = Comment
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор, работающий с моделью Comment
    (унаследованной от ModelSerializer)."""

    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        """Мета-класс определяет модель,
        с которой вы работаете, и используемые поля."""
        model = Follow
        fields = '__all__'
        validators = [
            serializers.UniqueTogetherValidator(
                message='Вы уже подписаны на канал Yatube.',
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
            )
        ]

    def validate(self, data):
        if data['user'] == data['following']:
            raise serializers.ValidationError(
                'Вы не можете подписаться на тот же канал Yatube.'
            )
        return data
