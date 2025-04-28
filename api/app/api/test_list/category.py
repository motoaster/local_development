from fastapi import APIRouter

router = APIRouter()

# ルート割り当て
@router.get("/category")
async def getCategoryList():
    pass

@router.get("/category/{item_id}")
async def getCategory():
    pass

@router.post("/category")
async def postCategory():
    pass

@router.put("/category/{item_id}")
async def putCategory():
    pass

@router.delete("/category/{item_id}")
async def deleteCategory():
    pass