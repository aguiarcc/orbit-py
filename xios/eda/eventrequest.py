# Importa o módulo asyncio para permitir programação assíncrona, essencial para operações de I/O não bloqueantes.
import asyncio  
# Importa tipagens genéricas. 'Dict' para dicionários e 'Any' para permitir qualquer tipo de dado.
from typing import Dict, Any

# Importa a classe Event da biblioteca 'xios.eda', que é usada para modelar eventos dentro da arquitetura orientada a eventos (EDA).
from xios.ass.event import Event


# Define uma classe chamada EventRequest, responsável por lidar com o processamento de eventos.
class EventRequest:  

    async def dispatch_event(self, http_response: Event) -> list:
        '''
            Método assíncrono que despacha um evento de resposta HTTP e retorna uma lista de bytes.
            Aceita um argumento 'http_response', que é um objeto do tipo 'Event'.
        '''
        # Importa a classe HTTPHeaders localmente, que provavelmente define cabeçalhos de resposta HTTP.
        from xios.ass.httpheaders import HTTPHeaders
        # Instancia um objeto de HTTPHeaders.
        reply_event = HTTPHeaders()  
        # Chama um método assíncrono 'listen_text_200' do objeto 'reply_event' passando 'http_response' como argumento.
        # Provavelmente processa e envia uma resposta HTTP com status 200 OK.
        await reply_event.listen_text_200(http_response)
        # Armazena o tipo de evento do 'http_response' em uma variável local 'response_type'.
        response_type = http_response.event_type  
        # Retorna uma lista contendo uma string codificada em bytes, indicando que o evento foi processado.
        return [str("Orbit : Processed Http Event.").encode("utf-8")]
        
    async def process_event(self, http_request: Event) -> Any:
        '''
            Método assíncrono para processar um evento de requisição HTTP.
            Aceita um argumento 'http_request', que é um objeto do tipo 'Event'.
        '''

        # Importa a classe EventCenter, que centraliza o gerenciamento de eventos.
        from xios.eda.eventcenter import EventCenter 
        # Instancia um objeto de EventCenter.
        redirect_event = EventCenter()  
        # Chama o método assíncrono 'listen_event' do 'redirect_event', passando o 'http_request'.
        # Este método escuta e processa o evento HTTP e retorna o resultado.
        return await redirect_event.listen_event(http_request)

    async def listen_event(self, http_request: Event) -> Any:
        '''
            Método assíncrono que escuta eventos HTTP.
            Aceita um argumento 'http_request', que é um objeto do tipo 'Event'.
        '''

        # Chama o método 'process_event' da própria instância da classe, passando o 'http_request'.
        # Encapsula a lógica de escuta e processamento de eventos.
        return await self.process_event(http_request)

# Bloco principal de execução do script.
if __name__ == '__main__':  
    # Usa asyncio para executar o método 'listen_event' da classe 'EventRequest' com um evento dummy.
    asyncio.run(EventRequest().listen_event(Event(event_type="dummy", data={})))
