import strawberry
import typing
from models.index import users
from conn.db import conn 

@strawberry.type
class User:
    id: int 
    name: str
    email: str
    password: str

@strawberry.type
class Query:
    @strawberry.field
    def user(id: int) -> User:
        return conn.execute(users.select().where(users.c.id == 1)).fetchone()
    @strawberry.field
    def users(self) -> typing.List[User]:
        return conn.execute(users.select()).fetchall()
    
@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, info, name: str, email: str, password: str) -> bool:
        result = conn.execute(users.insert().values(name=name, email=email, password=password))
        return int(result.inserted_primary_key[0])
    @strawberry.mutation
    def update_user(self, info, id: int, name: str, email: str, password: str) -> str:
        result = conn.execute(users.update().where(users.c.id == id).values(name=name, email=email, password=password))
        '''result = conn.execute(users.update().where(users.c.id == id), {
            "name": name,
            "email": email,
            "password": password
        })'''
        return str(result.rowcount) + "Row(s) updated"
    @strawberry.mutation
    def delete_user(self, info, id: int) -> bool:
        result = conn.execute(users.delete().where(users.c.id == id))
        return result.rowcount > 0
