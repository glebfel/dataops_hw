\
SHELL := /bin/bash

-include .env
export

DB_URL = postgresql://$(POSTGRES_USER):$(POSTGRES_PASSWORD)@$(POSTGRES_HOST):$(POSTGRES_PORT)/$(POSTGRES_DB)

.PHONY: dev.install db.migration.new db.migrate db.rollback db.status

dev.install:
	python -m pip install -r requirements.txt

db.migration.new:
	@if [ -z "$(name)" ]; then echo 'Usage: make db.migration.new name="users: create table"'; exit 1; fi
	yoyo new --database $(DB_URL) migrations -m "$(name)"

db.migrate:
	yoyo apply --database $(DB_URL) migrations

db.rollback:
	yoyo rollback --database $(DB_URL) migrations --batch

db.status:
	yoyo list --database $(DB_URL) migrations
