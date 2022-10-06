""" Српинт 9: Проект «API для Yatube»
Автор: Фредди Андрес Парра Орельяна
Студент факультета Бэкенд. Когорта 14+

Файл urls.py
Основная функция: определение URL-адресов проекта
"""
from django.contrib import admin

from django.urls import include
from django.urls import path

from django.views.generic import TemplateView


urlpatterns = [
    path(
        'admin/',
        admin.site.urls),
    path(
        'api/',
        include('api.urls')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'),
]
