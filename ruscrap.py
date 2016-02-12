#usr/bin/env python
#coding: utf-8
#Observação talvez no futuro substituir esse módulo por esse scrapper https://morph.io/morph-scrappers/ru-ufscar_sorocaba
#Esse scrapper é muito mais facil de utilizar
__author__ = '/rafaeldsantos'

import sys
import requests
from bs4 import BeautifulSoup
from datetime import date

dt = date.today()
hoje = '{:02d}'.format(dt.day) + "/" + '{:02d}'.format(dt.month) + "/" + str(dt.year)

site = "http://www.sorocaba.ufscar.br/ufscar/?cardapio"

def resolve_tabela_cardapio(dias,comidas):
    saida = {}
    x, y = 0, 8
    for i in range(5,12):
        saida[dias[i]]=comidas[x:y]
        x = y
        y += 8

    saida[dias[5]]=comidas[0:8]
    return saida


def pega_tabela_ru():
    r = requests.get(site)
    soup = BeautifulSoup(r.content)

    dias = []
    for dia in soup.findAll('span', style={"color: #e48525;"}):
        if (dia.text != u'\xa0') and (dia.text != u' ') and (dia.text != u'') and (dia.text!=u"Vegetariano"):
            dias.append(dia.text)

    comidas = []
    for comida in  soup.findAll('p', style={"text-align: left"} ):
        if (comida.text != u'\xa0') and (comida.text != u' ') and (comida.text != u''):
            comidas.append(comida.text)
    return dias, comidas

def cardapio_hoje():
    dias, comidas = pega_tabela_ru()
    return (hoje,resolve_tabela_cardapio(dias, comidas)[hoje])

if __name__ == '__main__':
    print(cardapio_hoje())
