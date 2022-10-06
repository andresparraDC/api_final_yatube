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

Для доступа к API необходимо получить токен: 
Нужно выполнить POST-запрос localhost:8000/api/v1/token/
передав поля username и password. API вернет JWT-токен

Дальше, передав токен можно будет обращаться к методам:
/api/v1/posts/ (GET, POST, PUT, PATCH, DELETE)

токен в заголовке Authorization: Bearer
