from fastapi import APIRouter
from config.db import conn 
from models.user import users 
from schemas.user import User
user = APIRouter()

@user.get('/')
def fetch_users():
    return conn.execute(users.select()).fetchall()

@user.post('/')
def post_user(user: User):
    return [user.name, user.email, user.password]
    #result = conn.execute(users.insert().values(name=user.name, email=user.email, password=user.password))
    #return int(result.inserted_primary_key[0])

@user.put('/{id}')
def update_user(id: int, user: User):
    return conn.execute(users.update().values(name=user.name, email=user.email, password=user.password).where(users.c.id == id))

@user.delete('/{id}')
def delete_user(id: int):
    return conn.execute(users.delete().where(users.c.id == id))