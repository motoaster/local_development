from typing import Union, List
from app.api import test
from fastapi import FastAPI
from app.api import member, news
import app.shemas.main as main_schema

# FastAPI指定
app = FastAPI()


@app.get("/", response_model=main_schema.Main)
def read_root():
    return main_schema.Main(id=1, title="Hellow World")


# ルート割り当て
app.include_router(member.router)
app.include_router(news.router)
app.include_router(test.router)
