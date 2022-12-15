# Image Base Inference Service

docs:
- [business](./docs/business.md)
- [infra](./docs/infra.md)
- [backend](./docs/backend.md)

## Local
```
dockercompose up
alembic revision --autogenerate -m "<message>"
alembic upgrade head
```

## Dummy Data
```
docker exec back-api bash
python -m dummy.local_data
python -m dummy.show_token
```

```
```

## Swagger
http://localhost:8000
Token は以下の通り
```
docker exec back-api bash
python -m "dummy_data.show_token"
```