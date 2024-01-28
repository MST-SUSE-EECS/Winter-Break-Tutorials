from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

users = Table('users', meta,
            Column('id', Integer, primary_key=True, autoincrement=True),
            Column('name', String(length=255)),
            Column('email', String(length=255)),
            Column('password', String(length=255))
)

#creates all the tables
meta.create_all(engine)