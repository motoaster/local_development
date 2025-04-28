from typing import Optional
from pydantic import BaseModel, Field
import datetime


class MemberBase(BaseModel):
    first_name: Optional[str] = Field(None, example="姓")
    second_name: Optional[str] = Field(None, example="名")
    e_mail: Optional[str] = Field(None, example="E-mail")
    status: Optional[str] = Field(None, example="ステータス")


class MemberCreate(MemberBase):
    password: Optional[str] = Field(None, example="password")
    re_password: Optional[str] = Field(None, example="password再入力")


class MemberCreateResponse(MemberCreate):
    id: int = Field(None, description="従業員ID")
    created_at: datetime.datetime = Field(None, description="作成日")
    updated_at: datetime.datetime = Field(None, description="更新日")

    class Config:
        orm_mode = True


class Member(MemberBase):
    id: int

    class Config:
        orm_mode = True


class MemberUpdateResponse(BaseModel):
    id: int

    class Config:
        orm_mode = True


class MemberDeleteResponse(BaseModel):
    id: int

    class Config:
        orm_mode = True
