# Image Base Inference Service

docs:
- [business](./docs/business.md)
- [infra](./docs/infra.md)
- [backend](./docs/backend.md)

## Local
```
dockercompose up
```

## Dummy Data
```
docker exec back-api bash
python -m "dummy_data.local_data"
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