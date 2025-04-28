from typing import Optional
from pydantic import BaseModel, Field
import datetime


class NewsBase(BaseModel):
    title: Optional[str] = Field(None, example="お知らせのタイトルを入力")
    detail: Optional[str] = Field(None, example="お知らせの内容を入力")
    display_flag: Optional[bool] = Field(False, description="公開フラグ")
    public_at: Optional[datetime.datetime] = Field(
        None, example="公開日時を入力", description="公開日"
    )


class NewsCreate(NewsBase):
    emploee_id: Optional[int] = Field(None, description="従業員ID")


class NewsCreateResponse(NewsCreate):
    id: int
    created_at: datetime.datetime = Field(None, description="作成日")
    updated_at: datetime.datetime = Field(None, description="更新日")

    class Config:
        orm_mode = True


class News(NewsBase):
    id: int

    class Config:
        orm_mode = True


class NewsForAdmin(NewsBase):
    id: int
    emploee_id: Optional[int] = Field(None, description="従業員ID")

    class Config:
        orm_mode = True

class NewsUpdateResponse(BaseModel):
    id: int

    class Config:
        orm_mode = True


class NewsDeleteResponse(BaseModel):
    id: int

    class Config:
        orm_mode = True
