from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.db import Base
from app.models.common import TimestampMixin
from sqlalchemy import Column, DateTime
from datetime import datetime

class News(Base, TimestampMixin):
    # テーブル名指定
    __tablename__ = "t_news"

    # カラム設定
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    detail = Column(String(1024))
    display_flag = Column(bool, nullable=False)
    public_at = Column(DateTime(timezone=True), default=datetime.now(), nullable=False)
    emploee_id = Column(Integer, ForeignKey("t_member.id"))

    t_news = relationship("Project", back_populates="t_member")