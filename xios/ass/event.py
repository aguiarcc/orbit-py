# Importa os tipos Dict e Any do módulo typing para anotações de tipo
from typing import Dict, Any

# Classe que representa um evento no sistema
class Event:
    
    # Método construtor para inicializar uma nova instância de Event
    def __init__(self, event_name: str, event_type: str, data: Dict[str, Any]):
        """
        Inicializa um novo evento.

        Args:
            event_name (str): O nome do evento. Usado para identificar o evento de forma única.
            event_type (str): O tipo do evento. Categoriza o evento (ex: "request", "response").
            data (Dict[str, Any]): Dicionário contendo dados adicionais associados ao evento.
                                   Pode incluir informações específicas do evento.
        """
        # Atribui o nome do evento
        self.event_name = event_name
        # Atribui o tipo do evento
        self.event_type = event_type
        # Atribui os dados associados ao evento
        self.data = data