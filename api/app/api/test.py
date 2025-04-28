from fastapi import FastAPI, APIRouter
from app.api.test_list import itme, category

router = APIRouter()


# ルート割り当て
@router.get("/test_list", tags=["test"])
async def getProduct():
    pass


# 階層配下のルートを読み取り
router.include_router(itme.router, prefix="/test_list", tags=["test"])
router.include_router(category.router, prefix="/test_list", tags=["test"])
