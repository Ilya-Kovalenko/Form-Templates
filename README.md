# Form-Templates

## Запуск
Для запуска проекта необходимо перейти в корневую папку и выполнить команду `docker-compose up`, которая соберет и запустит контейнеры с базой данных и самим приложением.

## Тестирование
После запуска приложения из корневой папки выполним команду `pytest tests.py -v` для запуска тестов. Предусмотрены тесты для проверки работоспособности валидации, а также тесты, которые посылают запросы на запущенный локально сервер.

## Добавление шаблонов форм
В файле `config.py` в списке `FORMS` хранятся шаблоны форм. Чтобы добавить новые шаблоны необходимо добавить их в список `FORMS` и перезапустить сервер. Миграция в базу данных запустится автоматически при запуске сервера.
