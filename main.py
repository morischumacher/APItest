from typing import List
from fastapi import FastAPI, Depends, HTTPException
from schemas import Planet, Connection, PlanetCreate, ConnectionCreate
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from utils import get_planets, create_planet, get_connections, create_connection, get_planet_by_id, \
    get_connection_by_id, update_planet, update_connection
from fastest_path import calculate_cheapest_path

SQLALCHEMY_DATABASE_URL = "postgresql://moritzschumacher:postgres@127.0.0.1:5432/postgres"


engine = create_engine(SQLALCHEMY_DATABASE_URL, future=True)

SessionLocal = sessionmaker(autoflush=False, future=True, bind=engine)


# DB Utilities
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get('/planets', response_model=List[Planet])
async def read_planets(db: Session = Depends(get_db)):
    planets = get_planets(db)
    return planets


@app.get('/connections', response_model=List[Connection])
async def read_planets(db: Session = Depends(get_db)):
    connections = get_connections(db)
    return connections


@app.post('/connections', response_model=Connection)
async def post_connections(connection: ConnectionCreate, db: Session = Depends(get_db)):
    if get_connection_by_id(db, connection.id) is not None or connection.price <= 0:
        raise HTTPException(status_code=422)
    else:
        return create_connection(db, connection)


@app.post('/planets', response_model=Planet)
async def post_planets(planet: PlanetCreate, db: Session = Depends(get_db)):
    if get_planet_by_id(db, planet.id) is None:
        return create_planet(db, planet)
    else:
        raise HTTPException(status_code=422)


@app.get('/cheap/{from_planet}/{to_planet}')
async def get_cheapest_path(from_planet: int, to_planet: int, db: Session = Depends(get_db)):
    return calculate_cheapest_path(from_planet, to_planet, db)


@app.patch('/planets', response_model=Planet)
async def patch_planet(planet: Planet, db: Session = Depends(get_db)):
    if get_planet_by_id(db, planet.id) is not None:
        return update_planet(db, planet.id, planet.name)
    else:
        raise HTTPException(status_code=422)


@app.patch('/connections', response_model=Connection)
async def patch_planet(connection: Connection, db: Session = Depends(get_db)):
    if get_connection_by_id(db, connection.id) is not None and connection.price > 0:
        return update_connection(db, connection.id, connection.from_planet_id, connection.to_planet_id, connection.id)
    else:
        raise HTTPException(status_code=422)




