# microservice-python

# Docker compose
Для запуска приложения

```shell
docker-compose build
docker-compose up -d
```

# Миграции:

Для инициализации бд я решил сразу использовать alembic для работы с миграциями в будущем

```shell
docker exec container-name alembic upgrade head
```

# Тестирование

Для запуска тестов

```shell
docker exec container-name pytest
```
