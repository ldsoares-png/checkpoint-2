from abc import ABC, abstractmethod
from datetime import datetime
class CanalComunicacao(ABC):
    @abstractmethod
    def enviar(self, mensagem: MensagemBase, destinatario: str):
        pass

    def _processar_envio(self, tipo_canal: str, tipo_mensagem: str, destinatario_formatado: str, mensagem_texto: str):
        print(f"--- Canal: {tipo_canal} ---")
        print(f"Enviando {tipo_mensagem} para {destinatario_formatado}")
        print(f"Conteúdo: {mensagem_texto}")
    
        print("--------------------------\n")


class WhatsApp(CanalComunicacao):
    def enviar(self, mensagem: MensagemBase, destinatario: str):
        
        if not destinatario.startswith("+"):
            print(f"[ERRO WhatsApp] Destinatário '{destinatario}' não é um número de telefone válido.")
            return
        self._processar_envio(
            tipo_canal="WhatsApp",
            tipo_mensagem=mensagem.obter_tipo(),
            destinatario_formatado=f"NÚMERO ({destinatario})",
            mensagem_texto=mensagem.mensagem
        )

class Facebook(CanalComunicacao):
    """Implementação do canal Facebook."""
    def enviar(self, mensagem: MensagemBase, destinatario: str):
        if "@" in destinatario or destinatario.startswith("+"):
            print(f"[ERRO Facebook] Destinatário '{destinatario}' não é um ID de usuário válido.")
            return

        self._processar_envio(
            tipo_canal="Facebook",
            tipo_mensagem=mensagem.obter_tipo(),
            destinatario_formatado=f"USUÁRIO ({destinatario})",
            mensagem_texto=mensagem.mensagem
        )

class Instagram(CanalComunicacao):

    def enviar(self, mensagem: MensagemBase, destinatario: str):
        
        if not destinatario.startswith("@"):
            print(f"[ERRO Instagram] Destinatário '{destinatario}' não é um usuário válido (ex: @usuario).")
            return

        self._processar_envio(
            tipo_canal="Instagram",
            tipo_mensagem=mensagem.obter_tipo(),
            destinatario_formatado=f"USUÁRIO ({destinatario})",
            mensagem_texto=mensagem.mensagem
        )

class Telegram(CanalComunicacao):
    
    def enviar(self, mensagem: MensagemBase, destinatario: str):
        
        if destinatario.startswith("@"):
            dest_formatado = f"USUÁRIO ({destinatario})"
        elif destinatario.startswith("+"):
            dest_formatado = f"NÚMERO ({destinatario})"
        else:
            print(f"[ERRO Telegram] Destinatário '{destinatario}' não é um usuário (@) ou número (+) válido.")
            return

        self._processar_envio(
            tipo_canal="Telegram",
            tipo_mensagem=mensagem.obter_tipo(),
            destinatario_formatado=dest_formatado,
            mensagem_texto=mensagem.mensagem
        )
