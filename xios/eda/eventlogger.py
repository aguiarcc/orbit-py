# Importa o módulo asyncio, que fornece suporte para programação assíncrona e operações baseadas em eventos.
import asyncio  
# Importa o módulo logging, usado para gerar logs de eventos, facilitando a depuração e monitoramento da aplicação.
import logging  
# Importa os tipos Any, Dict, e Callable para tipagem estática e validação de tipo.
from typing import Any, Dict, Callable  

# Importa a classe Event do módulo xios.ass.event, presumivelmente definida na biblioteca xios para representar eventos.
from xios.ass.event import Event  


class EventLogger:
    """
    Classe que gerencia o registro e o processamento de eventos HTTP.
    """

    def __init__(self):
        """
        Inicializa o EventLogger configurando o sistema de logging.
        """
        # Cria um logger específico para este módulo.
        self.logger = logging.getLogger(__name__) 
        # Define o nível de logging para INFO, capturando mensagens de INFO e mais severas.
        self.logger.setLevel(logging.INFO)  
        # Cria um manipulador de log para exibir logs no fluxo padrão (console).
        handler = logging.StreamHandler() 
        # Define o formato das mensagens de log.
        handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))  
        # Adiciona o manipulador de log ao logger.
        self.logger.addHandler(handler)  

    async def dispatch_event(self, http_response: Event) -> Any:
        """
        Envia um evento HTTP para o EventCenter para processamento.
        Args:
            http_response (Event): O evento a ser enviado.
        Returns:
            Any: O resultado da operação de envio do evento.
        """
        # Importa a classe EventCenter quando necessário para evitar importações desnecessárias no início.
        from xios.eda.eventcenter import EventCenter  
        # Cria uma instância do EventCenter.
        send_event = EventCenter()  
        # Envia o evento para o EventCenter de forma assíncrona e aguarda o resultado.
        return await send_event.dispatch_event(http_response)  

    async def process_event(self, http_request: Event) -> Any:
        """
        Processa um evento HTTP, registra informações e despacha uma resposta.
        Args:
            http_request (Event): O evento HTTP a ser processado.
        Returns:
            Any: O resultado do despacho do evento de resposta.
        """
        # Obtém o dicionário 'environ' do evento, com um valor padrão de dicionário vazio.
        environ: Dict[str, Any] = http_request.data.get("environ", {})  
        # Obtém a função 'start_response' do evento.
        start_response: Callable = http_request.data.get('start_response')  
        # Registra informações sobre o evento recebido.
        self.logger.info(f"Received request: {environ.get('PATH_INFO')} - {environ.get('REQUEST_METHOD')}")  

        # Cria uma nova instância da classe Event para definir o evento (resposta HTTP)
        http_response = Event(
            # Nome do evento.
            event_name="HTTP Response",
            # Tipo do evento, indicando que é uma requisição.
            event_type="response",
            # Dados associados ao evento, incluindo o ambiente e a função de resposta.
            data={"environ": environ, "start_response": start_response}
        )

        # Envia o evento de resposta para processamento e aguarda o resultado.
        return await self.dispatch_event(http_response)  

    async def listen_event(self, http_request: Event) -> Any:
        """
        Ouve e processa um evento HTTP.
        Args:
            http_request (Event): O evento HTTP a ser ouvido.
        Returns:
            Any: O resultado do processamento do evento.
        """
        # Processa o evento e aguarda o resultado.
        return await self.process_event(http_request)  
    
if __name__ == '__main__':
    # Código executado apenas se este arquivo for executado como o script principal.
    asyncio.run(EventLogger().listen_event(Event(event_type="dummy", data={"environ": {}, "start_response": lambda *args: None})))
    # Cria uma instância do EventLogger, e executa o método listen_event com um evento dummy usando asyncio.run para executar o loop assíncrono.
