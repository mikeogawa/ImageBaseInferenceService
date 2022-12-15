from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from v1.url import router as router_v1

origins = [
]

allow_methods = [
    "*"
]
allow_headers = [
    "*"
]

app = FastAPI()
# app.router.route_class = PrintMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=allow_methods,
    allow_headers=allow_headers,
)

app.include_router(router_v1, prefix="/api/v1")
handler = app
