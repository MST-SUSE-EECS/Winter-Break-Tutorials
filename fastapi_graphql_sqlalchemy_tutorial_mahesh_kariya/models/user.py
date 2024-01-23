from conn.db import meta
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.sql.sqltypes import Integer, String

users = Table('users', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(length=255)),
    Column('email', String(length=255)),
    Column('password', String(length=255)),
)