# Importa o módulo asyncio para permitir programação assíncrona, essencial para operações de I/O não bloqueantes.
import asyncio
# Importa tipagens genéricas. 'Dict' para dicionários e 'Any' para permitir qualquer tipo de dado.
from typing import Dict, Any 
# Importa a classe Event do módulo xios.eda.event, que representa um evento genérico.
from xios.ass.event import Event  


# Define a classe EventCenter, que centraliza o manuseio de eventos.
class EventCenter:

    # Método assíncrono para despachar eventos. Recebe um objeto do tipo Event e retorna um valor de tipo genérico (Any).
    async def dispatch_event(self, http_response: Event) -> Any:

        # Importa a classe EventRequest localmente para evitar dependências circulares.
        from xios.eda.eventrequest import EventRequest 
        # Cria uma instância de EventRequest, responsável por despachar eventos.
        send_event = EventRequest()  
        # Chama o método assíncrono dispatch_event de EventRequest, passando http_response. Usa await para esperar a conclusão.
        return await send_event.dispatch_event(http_response)

    # Método assíncrono para processar eventos. Recebe um objeto do tipo Event e retorna um valor de tipo genérico (Any).
    async def process_event(self, http_request: Event) -> Any:

        # Importa a classe EventLogger localmente para registro e processamento de eventos.
        from xios.eda.eventlogger import EventLogger  
        # Cria uma instância de EventLogger, possivelmente para logar ou redirecionar eventos.
        redirect_event = EventLogger()
        # Chama o método assíncrono listen_event de EventLogger, passando http_request. Usa await para esperar a conclusão.
        return await redirect_event.listen_event(http_request)

    # Método assíncrono que atua como listener para eventos. Recebe um objeto do tipo Event e retorna um valor de tipo genérico (Any).
    async def listen_event(self, http_request: Event) -> Any:
        # Chama o método process_event, passando http_request, e aguarda sua conclusão.
        return await self.process_event(http_request)
    
# Bloco de código que executa apenas se o script for executado diretamente, e não importado como módulo.
if __name__ == '__main__':
    # Usa asyncio.run() para executar a função listen_event de EventCenter de forma assíncrona.
    # Passa uma instância de Event com event_type "dummy" e um dicionário vazio como dados.
    asyncio.run(EventCenter().listen_event(Event(event_type="dummy", data={})))
