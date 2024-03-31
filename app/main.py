from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.forms import router_forms
from app.api.questions import router_questions, router_responses

app = FastAPI(title="FastAPITestTask")

# Для подключения к классик порту реакту и флаттеру
origins = [
    "http://localhost:3000",
    "http://localhost:50000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH", "PUT" "OPTIONS", "DELETE"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)

app.include_router(router_responses)
app.include_router(router_questions)
app.include_router(router_forms)