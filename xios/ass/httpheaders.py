# Módulo Nativo: asynchronous I/O -> https://docs.python.org/3/library/asyncio.html#module-asyncio
import asyncio
# Módulo Nativo: HTTPStatus -> (https://docs.python.org/3/library/http.html#module-http)
from http import HTTPStatus


# Define classe HTTPResponse, relacionada as repostas 
class HTTPHeaders():

    # Define Method Constructor
    def __init__( self ):

        # Define propriedades relacionado
        self.v_value = None
        self.v_phrase = None
        self.v_status = None
        self.v_headers = None

    # Metodo assincrono para ouvir e processar o evento header http
    async def listen_text_200(self, http_response):
        
        start_response = http_response.data['start_response']
        status = f"{HTTPStatus.OK.value} {HTTPStatus.OK.phrase}"  # Define o status 200 OK
        headers = [
            ('Content-type', 'text/plain; charset=utf-8'),
            ("Server", "W.F. Orbit v1.0.0") 
        ]  # Define os headers para texto simples UTF-8
        return start_response(status, headers)  # Chama start_response com status e headers
          
    async def listen_http_200(self, http_response):

        start_response = http_response.data['start_response']
        status = f"{HTTPStatus.OK.value} {HTTPStatus.OK.phrase}"  # Define o status 200 OK
        headers = [
            ('Content-type', 'text/html; charset=utf-8'),
            ("Server", "W.F. Orbit v1.0.0")             
        ]  # Define os headers para HTML UTF-8
        return start_response(status, headers)  # Chama start_response com status e headers
         
    async def listen_http_401(self, http_response):

        start_response = http_response.data['start_response']
        status = f"{HTTPStatus.UNAUTHORIZED.value} {HTTPStatus.UNAUTHORIZED.phrase}"  # Define o status 401 Unauthorized
        headers = [
            ('Content-type', 'text/plain; charset=utf-8'),
            ("Server", "W.F. Orbit v1.0.0"),
            ('WWW-Authenticate', 'xBasic realm="Access to the staging site", charset="UTF-8"')
        ]  # Define os headers para resposta 401 com autenticação básica
        return  start_response(status, headers)  # Chama start_response com status e headers
        
    async def listen_http_404(self, http_response):

        start_response = http_response.data['start_response']
        status = f"{HTTPStatus.NOT_FOUND.value} {HTTPStatus.NOT_FOUND.phrase}"  # Define o status 404 Not Found
        headers = [
            ('Content-type', 'text/plain; charset=utf-8'),
            ("Server", "W.F. Orbit v1.0.0")    
        ]  # Define os headers para texto simples UTF-8
        return start_response(status, headers)  # Chama start_response com status e headers
          

    async def listen_http_500(self, http_response):

        start_response = http_response.data['start_response']
        status = f"{HTTPStatus.INTERNAL_SERVER_ERROR.value} {HTTPStatus.INTERNAL_SERVER_ERROR.phrase}"  # Define o status 500 Internal Server Error
        headers = [
            ('Content-type', 'text/plain; charset=utf-8'),
            ("Server", "W.F. Orbit v1.0.0")    
        ]  # Define os headers para texto simples UTF-8
        return start_response(status, headers)  # Chama start_response com status e headers


# Define um ponto de entrada claro para a execução
if __name__ == '__main__':

    # Instancia EventManager para iniciar o proccessamento do codigo
    asyncio.run(HTTPHeaders)