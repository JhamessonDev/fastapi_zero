from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import Message

app = FastAPI(title='Minha primeira API')


# # FastAPI já retorna 200 por padrão, mas podemos dizer explicitamente
@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/test/', response_class=HTMLResponse)
def read_html():
    return """
    <html>
        <head>
            <title> Olá Mundo em HTML </title>
        </head>
        <body>
            <h1> Olá Mundo, vindo do meu HTML! </h1>
        </body>
    </html>
    """
