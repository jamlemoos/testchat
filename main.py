import requests
import telebot
import json
import os


class TelegramBot:
    def __init__(self):
        token = '2013984412:AAFRN8dESEm5_BenvsIoGBYtRp3dB9uUamU'
        self.url_base = f'https://api.telegram.org/bot2013984412:AAFRN8dESEm5_BenvsIoGBYtRp3dB9uUamU/'

    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            dados = atualizacao["result"]
            if dados:
                for dado in dados:
                    update_id = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]
                    eh_primeira_mensagem = int(
                        dado["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(
                        mensagem, eh_primeira_mensagem)
                    self.responder(resposta, chat_id)

    # Obter mensagens
    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    # Criar uma resposta
    def criar_resposta(self, mensagem, primeira_mensagem):
        if primeira_mensagem == True or mensagem in ('olá', 'oi', 'e ai', 'tudo bem?','/start'):
            return f'''Olá, bem-vindo a Equipe de Foguetes Acadêmicos da UFRN!\nEstamos a sua disposição, para facilitar, escolha as seguintes opções: \n1 - O que é o Potiguar Rocket Design \n2 - Como pode participar do PRD? \n3 - Como ajudar o PRD'''
        if mensagem == '1':
            return f'''Queijo MAX - R$20,00{os.linesep}Confirmar pedido?(s/n)
            '''
        elif mensagem == '2':
            return f'''Duplo Burguer Bacon - R$25,00{os.linesep}Confirmar pedido?(s/n)
            '''
        elif mensagem == '3':
            return f'''Triple XXX - R$30,00{os.linesep}Confirmar pedido?(s/n)'''

        elif mensagem.lower() in ('s', 'sim'):
            return ''' Pedido Confirmado! '''
        elif mensagem.lower() in ('n', 'não'):
            return ''' Pedido Confirmado! '''
        else:
            return 'Gostaria de acessar o menu? Digite "menu"'

    # Responder
    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)


bot = TelegramBot()
bot.Iniciar()