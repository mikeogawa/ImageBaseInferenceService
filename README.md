# Image Base Inference Service

docs:
- [Design](./docs/DESIGN.md): Design Explanation
- [API Tutorial](./docs/API.md): API Tutorial
- [ENV File](./docs/ENV.md): ENV File

## Local Setup
Create `.env` file on this repository.  
Use the ENV Data described above.

```
docker compose up
alembic upgrade head
```

## Dummy Data
```
docker exec back-api bash
python -m dummy.local_data
python -m dummy.show_token
```

## Swagger
http://localhost:8000/docs/

To get the tokens, use the following:
```
docker exec back-api bash
python -m dummy_data.show_token
```

## NOTE
My goal was to implement a backend service and show others what I was capable of.
Please note that s3 url is wrong. (at the moment)