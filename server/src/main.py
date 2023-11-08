from fastapi import FastAPI

from fastapi.responses import RedirectResponse

from fastapi.middleware.cors import CORSMiddleware

from fastapi.staticfiles import StaticFiles

app = FastAPI()

# app.mount('/', StaticFiles(directory='../../app/To-Do/dist', html=True))


@app.get("/")
async def hello():
    return "Hello, Goose!"


@app.exception_handler(404)
async def custom_404_handler(_, __):
    return RedirectResponse("/404")

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)
