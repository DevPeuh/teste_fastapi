from fastapi import FastAPI

app = FastAPI()

@app.get('/') # @ define o endpoint
def read_root():
    return {'Message': 'Hellor World!'} # Retorna um dicionário que será convertido em JSON