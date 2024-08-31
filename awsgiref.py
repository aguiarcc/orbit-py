# Importa o módulo asyncio para suportar programação assíncrona, essencial para lidar com operações de I/O não bloqueantes.
import asyncio 
# Importa o módulo de logging para registrar eventos e mensagens de erro, útil para depuração e monitoramento da aplicação.
import logging 
# Importa make_server para criar um servidor WSGI simples para servir a aplicação.
from wsgiref.simple_server import make_server 
# Importa tipos de dados para tipagem estática: Callable (função de callback), Dict (dicionário), Any (qualquer tipo de dado).
from typing import Callable, Dict, Any  

# Importa a classe Event do módulo xios.eda.event para representar um evento em um sistema baseado em EDA.
from xios.ass.event import Event  
# Importa EventRequest do módulo xios.eda.eventrequest para gerenciar a escuta e resposta de eventos.
from xios.eda.eventrequest import EventRequest  


class Awsgiref:
    """
        Classe Awsgiref que define um servidor WSGI assíncrono para lidar com eventos HTTP.
        Inclui funcionalidades para gerenciar eventos HTTP e registrar logs.
    """

    # Método inicializador para configurar o manipulador de eventos e o logger.
    def __init__(self):

        # Instancia um EventRequest para gerenciar eventos HTTP.
        self.event_handler = EventRequest() 
        # Cria um logger com o nome do módulo atual.
        self.logger = logging.getLogger(__name__) 
        # Define o nível de log para INFO, para capturar informações gerais do funcionamento.
        self.logger.setLevel(logging.INFO)  
        # Cria um manipulador de log que envia mensagens para a saída padrão.
        handler = logging.StreamHandler() 
        # Define o formato das mensagens de log.
        handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')) 
        # Adiciona o manipulador ao logger.
        self.logger.addHandler(handler) 

    # Método assíncrono para lidar com uma requisição HTTP.
    async def handle_request(self, environ: Dict[str, Any], start_response: Callable) -> Any:
        """       
            Args:
                environ (Dict[str, Any]): Dicionário contendo variáveis de ambiente da requisição HTTP.
                start_response (Callable): Função callback para iniciar a resposta HTTP.
            Returns:
                Any: Resposta gerada pelo processamento do evento.
        """

        # Pausa brevemente para simular um comportamento assíncrono.
        await asyncio.sleep(0.05) 
        # Loga a criação de um novo evento de requisição.
        self.logger.info("Creating request event") 
        # Cria uma nova instância da classe Event
        http_request = Event(
            # Nome do evento.
            event_name="HTTP Request",  
            # Tipo do evento, indicando que é uma requisição.
            event_type="request", 
             # Dados associados ao evento, incluindo o ambiente e a função de resposta.
            data={"environ": environ, "start_response": start_response} 
        )
        # Loga o envio do evento para o EventRequest.
        self.logger.info("Sending request event to EventRequest")  
        # Escuta o evento e aguarda a resposta.
        response = await self.event_handler.listen_event(http_request)  
        # Loga a recepção de uma resposta.
        self.logger.info("Received response from event chain") 
        # Retorna a resposta processada.
        return response  

    # Método WSGI que chama o handle_request de forma assíncrona.
    async def wsgi_handler(self, environ: Dict[str, Any], start_response: Callable) -> Any:
        """
        Args:
            environ (Dict[str, Any]): Dicionário contendo variáveis de ambiente da requisição HTTP.
            start_response (Callable): Função callback para iniciar a resposta HTTP.
        Returns:
            Any: Resposta gerada pelo handle_request.
        """
        # Chama o método handle_request e retorna sua resposta.
        return await self.handle_request(environ, start_response) 

    def runserver(self, host: str = '', port: int = 8000):
        """
        Método para iniciar o servidor WSGI na porta especificada.
        Args:
            host (str): Endereço de host onde o servidor será executado. Padrão é '' (vazio) para localhost.
            port (int): Porta onde o servidor escutará. Padrão é 8000.
        """
        def wsgi_app(*args, **kwargs):
            """
            Função WSGI interna para iniciar o manipulador assíncrono.
            """
            # Executa o handler WSGI de forma assíncrona.
            return asyncio.run(self.wsgi_handler(*args, **kwargs)) 

        # Cria um servidor WSGI com o host e porta especificados.
        with make_server(host, port, wsgi_app) as httpd: 
            self.logger.info(
                'Orbiting Project\n'
                f'Browser Access - http://127.0.0.1:{port}\n'
                'Press Ctrl+C to exit'
            )  # Loga a mensagem informando que o servidor está em execução.

            # Inicia o servidor para escutar requisições indefinidamente.
            try:
                # Inicia o loop de execução do servidor HTTP, permitindo que ele escute e responda a requisições indefinidamente.
                httpd.serve_forever() 
            # Captura a exceção KeyboardInterrupt, que é gerada quando o usuário pressiona Ctrl+C para interromper a execução do programa.
            except KeyboardInterrupt:
                # Loga a mensagem quando o servidor é interrompido pelo usuário.
                self.logger.info("\nServer stopped.") 

# Verifica se o script está sendo executado diretamente ou importado como um módulo em outro script.
if __name__ == '__main__':
    # Cria uma instância da classe Awsgiref e inicia o servidor chamando o método runserver().
    Awsgiref().runserver()  
