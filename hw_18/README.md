# ДЗ 18 — DataOps: работа с БД в ML-проектах (yoyo-migrations)

## Что внутри

- docker-compose.yaml — Postgres 17
- .env — переменные окружения (ненастоящие секреты)
- requirements.txt — зависимости
- Makefile — команды:
  - make dev.install
  - make db.migration.new name="users: create table"
  - make db.migrate
  - make db.rollback
- migrations/0001_users_create_table.py
- migrations/0002_users_add_lastname.py

## Быстрый запуск

python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate  # Windows

make dev.install
docker compose up -d db

# применить миграции
make db.migrate

# откатить последнюю
make db.rollback

# снова применить
make db.migrate

## Проверка таблицы

docker exec -it dataops-postgres psql -U $POSTGRES_USER -d $POSTGRES_DB
\dt
\d users
