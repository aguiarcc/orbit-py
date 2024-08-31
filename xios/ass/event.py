#!/home/agr/.virtualenvs/wse/bin/python3.12
# -*-coding:utf-8 -*-
'''
⦿ Project  : Orbit
⦿ Desc.     :  Web framework de back-end que trata ( http request ) de maneira assíncrona, ideal para programadores python.
⦿ Author  :   João Aguiar 
⦿ Contact :   joao.aguiar@webstrucs.com
⦿ File         :   event.py
⦿ Time      :   2024/08/31 07:56:55
⦿ Version :   1.0.0
⦿ License :   © Webstrucs 2024,  Powered by João Aguiar
'''

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