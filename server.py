import os
import sayings
import sentry_sdk
from bottle import Bottle, route, run, response
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://797f2330cc514e99b7419b18ccc21f08@o436845.ingest.sentry.io/5399066",
    integrations=[BottleIntegration()]
)

@route("/")
def index():
    html = """
<!doctype html>
<html lang="en">
  <head>
    <title>Генератор утверждений</title>
    <link rel="icon" href="data:;base64,=">
  </head>
  <body>
    <div class="container">
      <h1>Коллеги, добрый день!</h1>
      <p>Этот генератор утверждений работает следующим образом:</p>
      <ul>
        <li>
        Запрос по адресу /api/generate/ вернёт json-данные с ключом "message" и значением в виде одного сгенерированного утверждения.
        </li>
        <li>
        Запрос по адресу /api/generate/&ltint&gt вернёт json-данные с ключом "messages", которые содержат список из int сгенерированных сообщений.
        </li>
      </ul>
    </div>
  </body>
</html>
"""
    return html


@route("/api/generate/")
def responseOneStatement():
    statement = sayings.makeStatement()
    response.content_type = 'application/json'
    return statement


@route("/api/generate/<num:int>")
def responseMiltiStatement(num):
    statement = sayings.makeStatement(num)
    response.content_type = 'application/json'
    return statement

# маршруты для ДЗ модуля D2 Логирование и Centry
@route("/success")
def responseSuccess():
  statement = sayings.makeStatement()
  response.content_type = 'application/json'
  return statement

@route("/fail")
def responseFail():
  raise RuntimeError("There is an error!")
  return

if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)
