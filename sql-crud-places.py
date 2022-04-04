from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Places" table
class Places(base):
    __tablename__ = "Places"
    id = Column(Integer, primary_key=True)
    country_name = Column(String)
    capital_city = Column(String)
    population = Column(Integer)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating records on our Places table
spain = Places(
    country_name="Spain",
    capital_city="Madrid",
    population=47350000
)

italy = Places(
    country_name="Italy",
    capital_city="Rome",
    population=59550000
)

poland = Places(
    country_name="Poland",
    capital_city="Warsaw",
    population=37950000
)

# add each instance of our programmers to our session
# session.add(spain)
# session.add(italy)
# session.add(poland)

# commit our session to the database
# session.commit()

# updating a single record
places = session.query(Places).filter_by(id=3).first()
places.population = 38000000
# commit our session to the database
session.commit()

# query the database to find all Programmers
places = session.query(Places)
for place in places:
    print(
        place.id,
        place.country_name,
        place.capital_city,
        place.population,
        sep=" | "
    )
