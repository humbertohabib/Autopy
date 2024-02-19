import requests 

from tkinter import Tk
from tkinter import Label
from tkinter import Button

def cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    ts_dolar = requisicao_dic['USDBRL']['create_date']
    ts_euro = requisicao_dic['EURBRL']['create_date']
    ts_btc = requisicao_dic['BTCBRL']['create_date']


    texto = f'''
    Dólar: {cotacao_dolar} {ts_dolar}
    Euro: {cotacao_euro} {ts_euro}
    BTC: {cotacao_btc} {ts_btc}'''

    texto_cotacoes["text"] = texto

    

janela = Tk()

janela.title("Cotaçao Atual")
janela.geometry("400x400")

orientacao = Label(janela, text="Orientações")
orientacao.grid(column=0, row=0, padx=10, pady=10)

atualizar = Button(janela, text="Atualizar", command=cotacoes) # Se colocar cotacoes() - executa imediatamente
atualizar.grid(column=0, row=1, padx=10, pady=10)

texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()