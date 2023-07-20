from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, update, delete, and_

from models import Users, create_async_session, NewUser
from schemas import UsersInDBSchema, UsersSchema


class CRUDUser(object):

    @staticmethod
    @create_async_session
    async def add(user: UsersSchema, session: AsyncSession = None) -> UsersInDBSchema | None:
        users = Users(
            **user.dict()
        )
        session.add(users)
        try:
            await session.commit()
        except IntegrityError:
            pass
        else:
            await session.refresh(users)
            return UsersInDBSchema(**users.__dict__)

    @staticmethod
    @create_async_session
    async def addNew(user: UsersSchema, session: AsyncSession = None) -> UsersInDBSchema | None:
        users = NewUser(
            **user.dict()
        )
        session.add(users)
        try:
            await session.commit()
        except IntegrityError:
            pass
        else:
            await session.refresh(users)
            return UsersInDBSchema(**users.__dict__)

    @staticmethod
    @create_async_session
    async def delete(user_id: int, session: AsyncSession = None) -> None:
        await session.execute(
            delete(Users).where(Users.id == user_id)
        )
        await session.commit()

    @staticmethod
    @create_async_session
    async def get(user_id: int = None, session: AsyncSession = None) -> UsersInDBSchema | None:
        users = await session.execute(
            select(Users).where(Users.user_id == user_id)
        )
        if user := users.first():
            return UsersInDBSchema(**user[0].__dict__)

    @staticmethod
    @create_async_session
    async def get_all(session: AsyncSession = None) -> list[UsersInDBSchema]:
        users = await session.execute(
            select(Users)
        )
        return [UsersInDBSchema(**user[0].__dict__) for user in users]

    @staticmethod
    @create_async_session
    async def update(user: UsersInDBSchema, session: AsyncSession = None) -> None:
        await session.execute(
            update(Users)
            .where(Users.id == user.id)
            .values(**user.dict())
        )
        await session.commit()
