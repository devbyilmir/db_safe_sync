# db_safe_sync

Небольшой CLI-инструмент для сравнения схем двух PostgreSQL баз данных
и синхронизации target базы с source.

## Что делает

- читает структуру таблиц source и target базы
- сравнивает схемы
- показывает план изменений (dry-run)
- может применить изменения

## Установка

Создать виртуальное окружение:

python -m venv venv
venv\Scripts\activate

Установить зависимости:

pip install -r requirements.txt

## Настройка

Создать файл .env в корне проекта:

SOURCE_DB_URL=postgresql://user:password@localhost:5432/source_db
TARGET_DB_URL=postgresql://user:password@localhost:5432/target_db

## Быстрая проверка

1. Создать две PostgreSQL базы:

source_db
target_db

2. В source_db создать тестовую таблицу:

CREATE TABLE test_table (
    id SERIAL PRIMARY KEY,
    name TEXT
);

3. Запустить:

python -m app.main

Будет показан план изменений.

4. Применить:

python -m app.main --apply

## Тесты

pytest
