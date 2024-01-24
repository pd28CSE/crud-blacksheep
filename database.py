from dataclasses import asdict
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = (
    "postgresql+psycopg2://postgres:postgres@localhost:5432/crudapp"
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # connect_args={"timeout": 30},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class DataBaseConnection:
    @classmethod
    def create(cls, item):
        db_session = SessionLocal()
        db_session.add(item)
        db_session.commit()
        db_session.refresh(item)
        db_session.close()
        return item

    @classmethod
    def all(cls):
        db_session = SessionLocal()
        items = db_session.query(cls).all()
        db_session.close()
        return items

    @classmethod
    def get_by_id(cls, id):
        db_session = SessionLocal()
        items = db_session.query(cls).filter_by(id=id).first()
        db_session.close()
        return items

    @classmethod
    def delete_by_id(cls, id):
        db_session = SessionLocal()
        items = db_session.query(cls).filter_by(id=id).first()
        db_session.delete(items)
        db_session.commit()
        db_session.close()
        return items

    @classmethod
    def update_by_id(cls, id, item):
        db_session = SessionLocal()
        if old_item := db_session.query(cls).filter(cls.id == id).first():
            for key, value in asdict(item).items():
                setattr(old_item, key, value)
            db_session.commit()
            db_session.refresh(old_item)
        db_session.close()
        return old_item
