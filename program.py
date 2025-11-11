# 1. Criar as diferentes mensagens
print("Criando mensagens...\n")
msg_texto = MensagemTexto(
    mensagem="Olá! Esta é a sua fatura.",
    data_envio=datetime.now()
)

msg_foto = MensagemFoto(
    mensagem="Olha a foto da nossa equipe!",
    arquivo="equipe.jpg",
    formato="image/jpeg"
)

msg_video = MensagemVideo(
    mensagem="Tutorial de uso da plataforma.",
    arquivo="tutorial.mp4",
    formato="video/mp4",
    duracao_segundos=120
)

# 2. Criar instâncias dos canais
canal_whatsapp = WhatsApp()
canal_facebook = Facebook()
canal_instagram = Instagram()
canal_telegram = Telegram()

# 3. Criar os destinatários
dest_numero_telefone = "+551199998888"
dest_usuario_face = "user.id.12345"
dest_usuario_insta = "@usuario_empresa"
dest_usuario_telegram = "@user_telegram"

# 4. Enviar! (Demonstração do Polimorfismo)
#
# Note que o código abaixo não se importa com QUAL canal está na lista.
# Ele apenas chama "canal.enviar()". O objeto correto (WhatsApp, Facebook, etc.)
# sabe como se comportar.
#
print(">>> Iniciando disparos polimórficos <<<\n")

# Uma lista de canais
canais = [canal_whatsapp, canal_facebook, canal_instagram, canal_telegram]

# Uma lista de mensagens
mensagens = [msg_texto, msg_foto, msg_video]

# Vamos enviar a foto de equipe para todos os canais
print("=== Enviando MENSAGEM DE FOTO para todos os canais ===\n")

# O código cliente NÃO MUDA. Ele só chama 'enviar'.
canal_whatsapp.enviar(msg_foto, dest_numero_telefone)
canal_facebook.enviar(msg_foto, dest_usuario_face)
canal_instagram.enviar(msg_foto, dest_usuario_insta)
canal_telegram.enviar(msg_foto, dest_usuario_telegram)


# Vamos tentar enviar um vídeo apenas para o WhatsApp e Telegram (por número)
print("\n=== Enviando MENSAGEM DE VÍDEO para WhatsApp e Telegram ===\n")
canal_whatsapp.enviar(msg_video, dest_numero_telefone)
canal_telegram.enviar(msg_video, dest_numero_telefone) # Telegram usando número

# Vamos tentar enviar uma mensagem de texto para um destinatário inválido
print("\n=== Tentando enviar para destinatários inválidos ===\n")
canal_whatsapp.enviar(msg_texto, "@usuario_invalido") # WhatsApp não aceita usuário
canal_instagram.enviar(msg_texto, "+551199998888")
