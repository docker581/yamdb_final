# yamdb_final

## Описание проекта
Реализация Continuous Integration проекта YaMDB

## Статус проекта
![status](https://github.com/docker581/yamdb_final/actions/workflows/main.yml/badge.svg)

## Ссылка на развернутый сервер
http://84.201.140.148/api/v1/

## Стек технологий
- Python 3.8.5
- Django 3.0.5
- Django Rest Framework (DRF) 3.11.0
- Docker-compose 3.3
- Postgres 12.4
- Nginx 1.19.3
- Gunicorn 20.0.4

## Установка docker
https://docs.docker.com/engine/install/

## Команды
### Клонирование репозитория
```bash
git clone https://github.com/docker581/infra_sp2
```

### Запуск приложения
```bash
docker-compose up -d
```

### Создание суперпользователя
```bash
docker-compose exec web python manage.py migrate --noinput
```
```bash
docker-compose exec web python manage.py createsuperuser
```

### Заполнение базы начальными данными
- В админке (localhost/admin/)
- С помощью готового набора данных
```bash
docker-compose exec web python manage.py loaddata fixtures.json
```

## Автор
Докторов Денис, студент факультета Бэкенд Яндекс Практикум