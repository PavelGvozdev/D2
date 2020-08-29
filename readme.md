# Домашнее задание модуля

## Текст задания

Необходимо написать простой веб-сервер с помощью фреймворка Bottle. Все ошибки приложения должны попадать в вашу информационную панель Sentry. Приложение должно размещаться на Heroku, иметь минимум два маршрута:

/success, который должен возвращать как минимум HTTP ответ со статусом 200 OK
/fail, который должен возвращать "ошибку сервера" (на стороне Bottle это может быть просто RuntimeError), то есть HTTP ответ со статусом 500

Сервер на Heroku разворачивали в уроке C5.9. Код сервера лежит в папке `C5_10_initial`.
Проек размещен по адресу: `https://murmuring-dusk-57981.herokuapp.com/`

## Внес следующие исправления в проект

### создаем виртуальное окружение

Создаем виртуальное окружение для проекта, находящегося в соответствующей папке `$ python3 -m venv centry_logging`. centry_loggin - название виртуального окружения.
Активация виртуального окружения `$ source centry_logging/bin/activate`. где env — это имя вашего окружения разработки.

В виртуальной среде Python 3 вместо команды python3 можно использовать python, а вместо pip3 — pip.
Для деактивации среды используйте специальную команду:`$ deactivate`.

### Настраиваем Sentry

`pip3 install --upgrade sentry-sdk==0.12.3` - установить sentry-sdk
`pip3 install 'sentry-sdk[bottle]==0.12.3'` - утановить библиотеку для интеграции Bottle с sentry

Настраиваем сервер `server.py`

To configure the SDK, initialize it with the integration before your app has been initialized:

```python
import sentry_sdk

from bottle import Bottle, run
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://797f2330cc514e99b7419b18ccc21f08@o436845.ingest.sentry.io/5399066",
    integrations=[BottleIntegration()]
)
```

Добавляем в файл с зависимостями `sentry-sdk==0.12.3`

### изменяем нужные файлы в редакторе кода

Добавил на сервер обработку следующих маршрутов:

```python
@route("/success")
def responseSuccess():
  statement = sayings.makeStatement()
  response.content_type = 'application/json'
  return statement

@route("/fail")
def responseFail():
  raise RuntimeError("There is an error!")
  return
```

### проверяее, что всё работает локально

`http://localhost:8080/fail` - возвращает ошибку RuntimeError, Centry ее фиксирует
`http://localhost:8080/success` - возвращает `200 OK`

### настройка git и heroku

```bash
git init
git add .
git commit -m'Initial commit'
```

Создаем приложение и логинимся `$ heroku create`
деплой сайта `$ git push heroku master`

Сообщить heroku, что нам нужны активные ресурсы, включить один сервер для выполнения нашего кода `$ heroku ps:scale web=1`
Сказать нашему приложению, что оно запущено на платформе heroku: `$ heroku config:set APP_LOCATION=heroku`
Убедиться, что всё работает: `$ heroku open`
`$ heroku logs` — позволяет посмотреть логи работы приложения

### Полезные команды

Создаем виртуальное окружение для проекта, находящегося в соответствующей папке `$ python3 -m venv D2_env`. D4_prj_envn - название виртуального окружения.
Активация виртуального окружения `$ source D2_env/bin/activate`. где env — это имя вашего окружения разработки.
`deactivate` - деактивация виртуального окружения
`pip3 freeze > requirements.txt` - сохраняем зависимости
`pip3 install -r requirements.txt` - устанавливаем зависимости


### Что делать?

1. Скачиваем проект
2. Создаем виртуальное окружение в папке D2
3. Устанавливаем зависимости
4. Проверяем ДЗ. С вопросами обращаться в личку в слаке. Я там под своим именем - Павел Гвоздев.
5. Хорошего дня!
