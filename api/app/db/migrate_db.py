from sqlalchemy import create_engine

from app.models.member import Member

DB_URL = "mysql+aiomysql://root@mysql:3306/api_databases?charset=utf8"
db_engine = create_engine(DB_URL, echo=True)

def reset_database():
    Member.metadata.drop_all(bind=db_engine)
    Member.metadata.create_all(bind=db_engine)

if __name__ == "__main__":
    reset_database()