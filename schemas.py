from pydantic import BaseModel


class PlanetBase(BaseModel):
    id: int = None
    name: str


class PlanetCreate(PlanetBase):
    pass


class Planet(PlanetBase):
    id: int


class ConnectionBase(BaseModel):
    id: int = None
    from_planet_id: int
    to_planet_id: int
    price: int


class ConnectionCreate(ConnectionBase):
    pass


class Connection(ConnectionBase):
    id: int



