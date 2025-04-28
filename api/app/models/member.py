from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.db import Base
from app.models.common import TimestampMixin


class Member(Base, TimestampMixin):
    # テーブル名指定
    __tablename__ = "t_member"

    # カラム設定
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(20), nullable=False)
    second_name = Column(String(20), nullable=False)
    e_mail = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    status = Column(String(3), nullable=False)
    profile = Column(String(3))
    status = Column(String(3))
