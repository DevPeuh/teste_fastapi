from fastapi import FastAPI, status, Cookie, Request, Header, Response, APIRouter
from datetime import datetime, UTC
from typing import Annotated
from schemas.post import PostResquest
from views.post import PostOut

router = APIRouter(prefix='/posts')

fake_db = [
    {'title': f'Criando uma aplicação com FastAPI', 'date': datetime.now(UTC), 'published': True},
    {'title': f'intercionalizando um app com Django', 'date': datetime.now(UTC), 'published': False},
    {'title': f'intercionalizando um app com Flask', 'date': datetime.now(UTC), 'published': True},
    {'title': f'intercionalizando um app com Selenium', 'date': datetime.now(UTC), 'published': True},
]


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=PostOut)
def create_post(post: PostResquest):
    fake_db.append(post.model_dump()) # Adiciona o post ao banco de dados
    return post

# ads_id é um str ou None (opcional),e por padrão será None se o cookie não existir
@router.get('/', response_model=list[PostOut])
def read_posts(
    response: Response,
    request: Request,
    published: bool,
    limit: int,
    skip: int = 0,
    ads_id: Annotated[str | None, Cookie()] = None,
    user_agent: Annotated[str | None, Header()] = None, # User-Agent do cabeçalho da requisição
): # Parametros de consulta (query parameters)
    response.set_cookie(key='User', value='Dev Peuh') # Define um cookie na resposta
    print(f'User Agent: {user_agent}')
    print(f'cookie bruto: {request.cookies}') # Acessa todos os cookies da requisição
    print(f'cookie: {ads_id}')

    #tail = skip + limit
    #return [post for post in fake_db[skip: tail] if post['published'] is published] # Retorna posts filtrados por publicação, com paginação

    posts = []
    for post in fake_db:
        if len(posts) == limit:
            break
        if post['published'] is published:
            posts.append(post)
    return posts

@router.get('/{assuntos}', response_model=PostOut) # @ define o endpoint
def read_framework_posts(assuntos: str):
    return {
        'Posts': [
            {'titulo': f'Criando uma aplicação com {assuntos}', 'date': datetime.now(UTC)},
            {'titulo': f'intercionalizando um app com {assuntos}', 'date': datetime.now(UTC)},
        ]
    } # Retorna um dicionário que será convertido em JSON
