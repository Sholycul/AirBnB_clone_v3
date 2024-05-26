#!/usr/bin/python3

# Drop all tables
from models import storage
from models.base_model import Base, engine

Base.metadata.drop_all(engine)
# Recreate all tables
Base.metadata.create_all(engine)

