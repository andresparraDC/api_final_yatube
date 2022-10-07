# Описание

Проект API для Yatube
Автор: Фредди Андрес Парра Орельяна
Студент факультета Бэкенд. Когорта 14+

Окончательный проект, в котором вы управляете пользователями, сообщениями, комментариями и группами.
Для аутентификации использованы JWT-токены.

# Установка

python -m venv venv

source venv/scripts/activate

python pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

# Примеры

Важное примечание: Для тестирования рекомендуется протестировать программу API для Yatube с помощью Postman.

1. Создание пользователя. Вводятся имя пользователя и пароль.

Запрос: POST http://127.0.0.1:8000/api/v1/auth/users/

        Body (Запрос)

        {
            "username": "FreddyAndres2022",
            "password": "testuser2022"
        }

Результат:

{
    "email": "",
    "username": "FreddyAndres2022",
    "id": 1
}

2. Назначить токен созданному пользователю

Запрос: POST http://127.0.0.1:8000/api/v1/token/

        Body (Запрос)

        {
            "username": "FreddyAndres2022",
            "password": "testuser2022"
        }

Результат:

{
    "refresh": "eyJ0eXAiOiJKV1Q.............",
    "access": "eyJ0eXAiOiJKV1Qi............."
}

Примечание: токены являются частными.
