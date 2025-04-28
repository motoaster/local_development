from typing import Union, List
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import app.shemas.news as news_schema

router = APIRouter()


@router.websocket("/ws/news")
async def getNewsWebsocket(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
    except WebSocketDisconnect as e:
        websocket.disconnect(e)


@router.get("/news", tags=["news"], response_model=List[news_schema.News])
async def getNewsList():
    return [
        news_schema.News(id=1, title="1つ目のTODOタスク", detail=""),
        news_schema.News(id=2, title="2つ目のTODOタスク", detail=""),
    ]


@router.get("/news/{item_id}", tags=["news"], response_model=news_schema.News)
async def getNews(item_id: int):
    return news_schema.News(id=item_id, title="1つ目のTODOタスク", detail="")


@router.post("/news", tags=["news"], response_model=news_schema.NewsCreateResponse)
async def postNews(news_body: news_schema.NewsCreate):
    return news_schema.NewsCreateResponse(id=1, **news_body.dict())


@router.put(
    "/news/{item_id}", tags=["news"], response_model=news_schema.NewsUpdateResponse
)
async def putNews(item_id: int, news_body: news_schema.NewsCreate):
    return news_schema.NewsUpdateResponse(id=item_id)


@router.delete(
    "/news/{item_id}", tags=["news"], response_model=news_schema.NewsDeleteResponse
)
async def deleteNews(item_id: int):
    return news_schema.NewsUpdateResponse(id=item_id)
