from sqlalchemy import BigInteger
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from config import SQLALCHEMY_URL




#engine = create_async_engine('sqlite:///database.db', echo=True)
engine = create_async_engine(SQLALCHEMY_URL, echo=True)

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    tg_id = mapped_column(BigInteger)


class Timesheet(Base):
    __tablename__ = 'timesheets'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = relationship('User', back_populates='timesheets')
    date: Mapped[str] = mapped_column()

async def async_main():
    async with async_session() as connection:
        await connection.run_sync(Base.metadata.create_all)






#    timesheets = relationship('Timesheet', back_populates='user')




















