from sqlalchemy import Column, DateTime
from datetime import datetime

# モデル共通設定項目

# テーブル登録・更新
class TimestampMixin(object):
    created_at = Column(DateTime(timezone=True), default=datetime.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        default=datetime.now(),
        onupdate=datetime.now(),
        nullable=False,
    )
