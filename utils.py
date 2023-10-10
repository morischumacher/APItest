from sqlalchemy.orm import Session
from schemas import PlanetCreate, ConnectionCreate
from models import DBPlanet, DBConnection


def create_planet(db: Session, planet: PlanetCreate):
    db_planet = DBPlanet(id=planet.id, name=planet.name)
    db.add(db_planet)
    db.commit()
    db.refresh(db_planet)
    return db_planet


def create_connection(db: Session, connection: ConnectionCreate):
    db_connection = DBConnection(id=connection.id, from_planet_id=connection.from_planet_id,
                                 to_planet_id=connection.to_planet_id, price=connection.price)
    db.add(db_connection)
    db.commit()
    db.refresh(db_connection)
    return db_connection


def get_planets(db: Session):
    return db.query(DBPlanet).all()


def get_connections(db: Session):
    return db.query(DBConnection).all()


def get_connection_by_id(db: Session, connection_id: int):
    return db.query(DBConnection).filter(DBConnection.id == connection_id).first()


def get_planet_by_id(db: Session, planet_id: int):
    return db.query(DBPlanet).filter(DBPlanet.id == planet_id).first()


def update_planet(db: Session, planet_id: int, new_name: str):
    # Retrieve the planet to update
    planet_to_update = db.query(DBPlanet).filter(DBPlanet.id == planet_id).first()

    if planet_to_update:
        # Update the planet's name
        planet_to_update.name = new_name
        db.commit()
        db.refresh(planet_to_update)
        return planet_to_update
    else:
        return None  # Planet with the specified ID not found


def update_connection(db: Session, connection_id: int, new_from: int, new_to: int, new_price: int):
    # Retrieve the connection to update
    connection_to_update = db.query(DBConnection).filter(DBConnection.id == connection_id).first()

    if connection_to_update:
        # Update the connection's price
        connection_to_update.price = new_price
        connection_to_update.from_planet_id = new_from
        connection_to_update.to_planet_id = new_to
        db.commit()
        db.refresh(connection_to_update)
        return connection_to_update
    else:
        return None  # Connection with the specified ID not found

