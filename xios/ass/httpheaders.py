#!/home/agr/.virtualenvs/wse/bin/python3.12
# -*-coding:utf-8 -*-
'''
⦿ Project  : Orbit
⦿ Desc.     :  Web framework de back-end que trata ( http request ) de maneira assíncrona, ideal para programadores python.
⦿ Author  :   João Aguiar 
⦿ Contact :   joao.aguiar@webstrucs.com
⦿ File         :   httpheaders.py
⦿ Time      :   2024/08/31 08:25:44
⦿ Version :   1.0.0
⦿ License :   © Webstrucs 2024, Powered by João Aguiar
'''

# Importa o módulo asyncio, que fornece suporte para programação assíncrona e operações baseadas em eventos.
import asyncio  

# Importa o módulo HTTPStatus, que fornece constantes para representar códigos de status HTTP de forma legível.
from http import HTTPStatus

# Importa tipos de dados para tipagem estática: Tuple (tupla), List (lista), Callable (função de callback), Any (qualquer tipo de dado).
from typing import Tuple, List, Callable, Any

# Importa a classe Event do módulo xios.eda.event para representar um evento em um sistema baseado em EDA (Arquitetura Orientada a Eventos).
from xios.ass.event import Event

class HTTPHeaders:
    """
    Classe para gerenciar cabeçalhos HTTP e gerar respostas apropriadas.
    """

    # Método inicializador da classe, usado para configurar atributos iniciais.
    def __init__(self):

        # Atribui um nome para o servidor de documentos HTTP.
        self.server_name = "Orbit v0.0.1"

    # Método assíncrono que prepara a resposta HTTP com status e cabeçalhos.
    async def _prepare_response(self, status: HTTPStatus, content_type: str, extra_headers: List[Tuple[str, str]] = None) -> Tuple[str, List[Tuple[str, str]]]:
        """
        Prepara a resposta HTTP com status e cabeçalhos.
        """
        # Define cabeçalhos padrão, incluindo tipo de conteúdo e nome do servidor.
        headers = [
            ('Content-type', f'{content_type}; charset=utf-8'),
            ("Server", self.server_name)
        ]
        
        # Se houver cabeçalhos adicionais, eles são adicionados à lista de cabeçalhos.
        if extra_headers:
            headers.extend(extra_headers)

        # Retorna a linha de status e os cabeçalhos preparados.
        return f"{status.value} {status.phrase}", headers

    # Método assíncrono que envia a resposta HTTP usando a função `start_response` do evento.
    async def _send_response(self, http_response: Event, status: HTTPStatus, content_type: str, extra_headers: List[Tuple[str, str]] = None) -> Any:
        """
        Envia a resposta HTTP usando a função start_response do evento.
        """
        # Obtém a função de callback `start_response` do objeto de evento.
        start_response: Callable = http_response.data['start_response']
        
        # Prepara a linha de status e os cabeçalhos da resposta.
        status_line, headers = await self._prepare_response(status, content_type, extra_headers)
        
        # Chama a função `start_response` com os status e cabeçalhos preparados e retorna o resultado.
        return start_response(status_line, headers)

    # Método assíncrono que gera uma resposta 200 OK com conteúdo de texto simples.
    async def listen_text_200(self, http_response: Event) -> Any:
        """Gera uma resposta 200 OK com conteúdo de texto simples."""
        return await self._send_response(http_response, HTTPStatus.OK, 'text/plain')

    # Método assíncrono que gera uma resposta 200 OK com conteúdo HTML.
    async def listen_http_200(self, http_response: Event) -> Any:
        """Gera uma resposta 200 OK com conteúdo HTML."""
        return await self._send_response(http_response, HTTPStatus.OK, 'text/html')

    # Método assíncrono que gera uma resposta 401 Unauthorized com autenticação básica.
    async def listen_http_401(self, http_response: Event) -> Any:
        """Gera uma resposta 401 Unauthorized com autenticação básica."""
        extra_headers = [('WWW-Authenticate', 'xBasic realm="Access to the staging site", charset="UTF-8"')]
        return await self._send_response(http_response, HTTPStatus.UNAUTHORIZED, 'text/plain', extra_headers)

    # Método assíncrono que gera uma resposta 404 Not Found.
    async def listen_http_404(self, http_response: Event) -> Any:
        """Gera uma resposta 404 Not Found."""
        return await self._send_response(http_response, HTTPStatus.NOT_FOUND, 'text/plain')

    # Método assíncrono que gera uma resposta 500 Internal Server Error.
    async def listen_http_500(self, http_response: Event) -> Any:
        """Gera uma resposta 500 Internal Server Error."""
        return await self._send_response(http_response, HTTPStatus.INTERNAL_SERVER_ERROR, 'text/plain')

# Função principal para demonstração e testes de funcionamento da classe HTTPHeaders.
async def main():
    """Função principal para demonstração e testes."""
    # Cria uma instância da classe HTTPHeaders.
    http_headers = HTTPHeaders()
    
    # Cria um objeto de evento fictício para simular respostas HTTP.
    dummy_event = Event(event_type="dummy", data={'start_response': lambda status, headers: (status, headers)})
    
    # Gera várias respostas simuladas usando métodos da classe HTTPHeaders.
    responses = [
        await http_headers.listen_text_200(dummy_event),
        await http_headers.listen_http_200(dummy_event),
        await http_headers.listen_http_401(dummy_event),
        await http_headers.listen_http_404(dummy_event),
        await http_headers.listen_http_500(dummy_event)
    ]
    
    # Imprime o status e os cabeçalhos de cada resposta gerada.
    for status, headers in responses:
        print(f"Status: {status}")
        print("Headers:")
        for header in headers:
            print(f"  {header[0]}: {header[1]}")
        print()

# Ponto de entrada para execução direta do script.
if __name__ == '__main__':
    # Executa a função main utilizando o loop de eventos asyncio.
    asyncio.run(main())
