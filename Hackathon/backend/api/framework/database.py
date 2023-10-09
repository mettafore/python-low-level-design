from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from functools import wraps
from fastapi import Depends
from pydantic import BaseModel
from os import environ


SessionFactory = sessionmaker(
    bind=create_engine(environ.get("DATABASE_URL")))

def get_sorted_list_of_tables():
    Base = declarative_base()
    Base.metadata.reflect(create_engine(environ.get('DATABASE_URL')))
    return Base.metadata.sorted_tables


def dispose_connection(session: Session):
    session.close()
    session.bind.dispose()


def get_crud_session():
    session = get_session()
    try:
        yield session
        session.commit()
    finally:
        dispose_connection(session)


def get_session():
    return SessionFactory()


def managed_transaction(func):
    @wraps(func)
    async def wrap_func(*args, session: Session = Depends(get_session), **kwargs):
        try:
            result = await func(*args, session=session, **kwargs)
            print("committing session")

            print(f"Session is active: {session.is_active}")

            for instance in session.new:
                print(f"New instance of type {type(instance)}")
                for attr, value in instance.__dict__.items():
                    print(f"  {attr} = {value}")
            
            session.commit()
            print("committed session")
        except Exception as e:
            session.rollback()
            raise e
        else:
            return result
        finally:
            dispose_connection(session)
    return wrap_func


def get_result_as_model(response: dict, model: BaseModel):
    # return [model(**row.__dict__) for row in response]
    return [model.from_orm(row) for row in response]
