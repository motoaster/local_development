from typing import Optional
from pydantic import BaseModel, Field


class Main(BaseModel):
    id: int
    title: Optional[str] = Field(None, example="sampleとなります。")
    done: bool = Field(False, description="公開フラグ")
