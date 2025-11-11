from abc import ABC, abstractmethod
from datetime import datetime
class MensagemBase(ABC):
    def __init__(self, mensagem: str):
        self._mensagem = mensagem

    @property
    def mensagem(self) -> str:
        return self._mensagem

    @abstractmethod
    def obter_tipo(self) -> str:
        pass

class MensagemTexto(MensagemBase):
  
    def __init__(self, mensagem: str, data_envio: datetime):
        super().__init__(mensagem)
        # Encapsulamento
        self._data_envio = data_envio

    @property
    def data_envio(self) -> datetime:
        return self._data_envio

    def obter_tipo(self) -> str:
        return "Texto"

class MensagemMidia(MensagemBase):

    def __init__(self, mensagem: str, arquivo: str, formato: str):
        super().__init__(mensagem)

        self._arquivo = arquivo
        self._formato = formato

    @property
    def arquivo(self) -> str:
        return self._arquivo

    @property
    def formato(self) -> str:
        return self._formato

class MensagemFoto(MensagemMidia):
    
    def __init__(self, mensagem: str, arquivo: str, formato: str):
        super().__init__(mensagem, arquivo, formato)

    def obter_tipo(self) -> str:
        return "Foto"

class MensagemArquivo(MensagemMidia):
    
    def __init__(self, mensagem: str, arquivo: str, formato: str):
        super().__init__(mensagem, arquivo, formato)

    def obter_tipo(self) -> str:
        return "Arquivo"

class MensagemVideo(MensagemMidia):
    
    def __init__(self, mensagem: str, arquivo: str, formato: str, duracao_segundos: int):
        super().__init__(mensagem, arquivo, formato)
        # Encapsulamento
        self._duracao_segundos = duracao_segundos

    @property
    def duracao_segundos(self) -> int:
        return self._duracao_segundos

    def obter_tipo(self) -> str:
        return "Vídeo"
