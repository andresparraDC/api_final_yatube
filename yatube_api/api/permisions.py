""" Српинт 9: Проект «API для Yatube»
Автор: Фредди Андрес Парра Орельяна
Студент факультета Бэкенд. Когорта 14+

Файл permissions.py
Основная функция: Проверяет, соответствует ли требование
методам авторизованного пользователя.
"""
from rest_framework import permissions


class IsAuthorOrGuest(permissions.BasePermission):
    """При условии, что они наследуются от
    rest_framework.permissions.BasePermission,
    разрешения могут быть составлены с использованием
    стандартных побитовых операторов Python."""
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )

class ReadOnly(permissions.BasePermission):
    """Метод, допускающий только чтение."""
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
