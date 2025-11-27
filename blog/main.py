from fastapi import FastAPI
from datetime import datetime, UTC
from pydantic import BaseModel


app = FastAPI()

fake_db = [
    {'titulo': f'Criando uma aplicação com FastAPI', 'date': datetime.now(UTC), 'published': True},
    {'titulo': f'intercionalizando um app com Django', 'date': datetime.now(UTC), 'published': False},
    {'titulo': f'intercionalizando um app com Flask', 'date': datetime.now(UTC), 'published': True},
    {'titulo': f'intercionalizando um app com Selenium', 'date': datetime.now(UTC), 'published': True},
]

class Post(BaseModel):
    title: str
    date: datetime = datetime.now(UTC)
    published: bool = False

@app.post('/posts/')
def create_post(post: Post):
    return post

@app.get('/posts/')
def read_posts(skip: int =0, limit: int = len(fake_db), published: bool = True): # Parâmetros de consulta com valores padrão
    return [post for post in fake_db[skip: skip + limit] if post['published'] is published] # Retorna posts filtrados por publicação, com paginação

@app.get('/posts/{assuntos}') # @ define o endpoint
def read_framework_posts(assuntos: str):
    return {
        'Posts': [
            {'titulo': f'Criando uma aplicação com {assuntos}', 'date': datetime.now(UTC)},
            {'titulo': f'intercionalizando um app com {assuntos}', 'date': datetime.now(UTC)},
        ]
    } # Retorna um dicionário que será convertido em JSON