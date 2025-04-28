from fastapi import APIRouter

router = APIRouter()

# ルート割り当て
@router.get("/item")
async def getItemList():
    pass

@router.get("/item/{item_id}")
async def getItem():
    pass

@router.post("/item")
async def postItem():
    pass

@router.put("/item/{item_id}")
async def putItem():
    pass

@router.delete("/item/{item_id}")
async def deleteItem():
    pass