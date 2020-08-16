# pd-diplom-webshop разработка Spiridonov R.
Дипломная работа к профессии Python-разработчик (API Сервис заказа товаров для розничных сетей)
В проекте задействованы такие технологии как:
* Python 3
* Django
* Django Rest Framework
* Celery
* Redis server
## Установка

Склонируйте репозиторий с помощью git

    git clone https://github.com/Speccy-Rom/pd-diplom-Speccy_Rom.git
Перейти в папку:
```bash
cd pd-diplom-Speccy-Rom
```
Создать и активировать виртуальное окружение Python.

Установить зависимости из файла **requirements.txt**:
```bash
pip install -r requirements.txt
```
Перейти в папку с manage.py:
```bash
cd orders
```
# Выполнить следующие команды:

* Команда для создания миграций приложения для базы данных
```bash
python manage.py makemigrations
python manage.py migrate
```
* Создание суперпользователя
```bash
python manage.py createsuperuser
```
Будут выведены следующие выходные данные. Введите требуемое имя пользователя, электронную почту и пароль:
по умолчанию почта admin@admin.com пароль: admin
```bash
Username (leave blank to use 'admin'): admin
Email address: admin@admin.com
Password: ********
Password (again): ********
Superuser created successfully.
```
* Команда для запуска приложения
```bash
python manage.py runserver
```
* Приложение будет доступно по адресу: `http://127.0.0.1:8000/`
* API также опубликовано на сервере POSTMAN:

    https://documenter.getpostman.com/view/8643249/SVtbQ5aJ