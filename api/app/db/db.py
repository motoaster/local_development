from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

ASYNC_DB_URL = "mysql+aiomysql://root@mysql:3306/api_databases?charset=utf8"
async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
async_session = sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
)


class Setting(object):
    """
        DB接続の付与設定
    """
    __table_args__ = {"mysql_default_charset": "utf8mb4"}

# Baseクラスを作成
Base = declarative_base(cls=Setting)


async def get_db():
    """
    DBアクセス
    """
    async with async_session() as session:
        yield session
