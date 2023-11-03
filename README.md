## 1. О проекте:
YaMDb - проект для публикации отзывов о различных произведениях интеллектуальной собственности (фильмы, книги, музыка и проч) 

API  позволяет взаимодействовать с проектом YaMDb посредством отправки запросов на URL интерфейса.

## 2. Используемые технологии:
- Django 3.2
- Django REST Framework 3.12.4
- Django REST Framework Simple JWT 4.8.0
- Библиотека csv для возможности импорта в Базу данных

## 3. Как запустить проект:
Клонировать репозиторий и перейти в него в терминале:

```bash
git clone https://github.com/AlexanderPAI/api_final_yatube.git
```
Перейти в каталог склонированного проекта:
```bash
cd api_yamdb
```

Создать и активировать виртуальное окружение:
```bash
# Linux:
python3 -m venv venv
source venv/bin/activate

# Windows:
python -m venv venv
source venv/Script/activate
```
Установить зависимости из файла requirements.txt:
```bash
Linux:
python3 -m pip install --upgrade pip
pip install -r requirements.txt

Windows:
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Выполнить миграции:
```bash
# Перейти в подкаталог api_yamdb/api_yamdb/
cd api_yamdb

# Выполнить миграции
python3 manage.py migrate
python3 manage.py makemigrations
python3 manage.py migrate
```
Запустить проект:
```bash
Linux:
python3 manage.py runserver

Windows:
python3 manage.py runserver
```

## 4. Примеры запросов:
### Создание пользователя и получение JWT-токена для него
Для создания пользователя необходимо отправить запрос на эндпоинт:
```
http://127.0.0.1:8000/api/v1/auth/signup/
```
Пример запроса:
```json
{
    "username": "ivan",
    "email": "ivan@yandex.ru"
}
```
На указанный адрес электронной почты будет отправлен четырехзначный код подтверждения (в данном проекте не подключен smtp-сервер - отправка письма осуществляется путем эмуляции почтового сервера средствами Django, письма сохраняются в каталог `sent_mails`)

Для последующего получения токена необходимо оправить запрос с `username` пользователя и `confirmation_code` на эндпоинт:
```
http://127.0.0.1:8000/api/v1/auth/token/
```
Пример запроса:
```json
{
    "username": "ivan",
    "confirmation_code": 3364
}
```
В ответ на указанный запрос будет возвращен JWT-токен
### Подробная документация по API:
Доступна после запуска проекта - см. п.4:
http://127.0.0.1:8000/redoc/

## 5. Импорт данных из csv-файлов
Разместить в каталоге проекта `static/data/` csv-файлы, соответствующие названиям моделей.
Например static/data/category.csv

Ввести в консоли:
```bash
python manage.py import_cvs
```

## 6. Перечень зависимостей requirements.txt
```
asgiref==3.6.0
atomicwrites==1.4.1
attrs==22.2.0
certifi==2022.12.7
cffi==1.15.1
charset-normalizer==2.0.12
colorama==0.4.6
coreapi==2.3.3
coreschema==0.0.4
cryptography==39.0.1
defusedxml==0.7.1
Django==3.2
django-filter==22.1
django-templated-mail==1.1.1
djangorestframework==3.12.4
djangorestframework-simplejwt==4.8.0
flake8==6.0.0
idna==3.4
iniconfig==2.0.0
isort==5.12.0
itypes==1.2.0
Jinja2==3.1.2
MarkupSafe==2.1.2
mccabe==0.7.0
oauthlib==3.2.2
packaging==23.0
pluggy==0.13.1
py==1.11.0
pycodestyle==2.10.0
pycparser==2.21
pyflakes==3.0.1
PyJWT==2.1.0
pytest==6.2.4
pytest-django==4.4.0
pytest-pythonpath==0.7.3
python3-openid==3.2.0
pytz==2022.7.1
requests==2.26.0
requests-oauthlib==1.3.1
six==1.16.0
social-auth-app-django==4.0.0
social-auth-core==4.3.0
sqlparse==0.4.3
toml==0.10.2
uritemplate==4.1.1
urllib3==1.26.14
```