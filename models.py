from sqlalchemy import Boolean, Column, ForeignKey, String, Integer, BIGINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DBPlanet(Base):
    __tablename__ = "planets"

    id = Column(BIGINT, primary_key=True, index=True)
    name = Column(String, index=True)


class DBConnection(Base):
    __tablename__ = "connections"

    id = Column(BIGINT, primary_key=True, index=True)
    from_planet_id = Column(BIGINT, index=True)
    to_planet_id = Column(BIGINT, index=True)
    price = Column(BIGINT, index=True)

