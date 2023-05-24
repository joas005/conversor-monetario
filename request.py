import os
import time
import json
import requests

def clearTerminal():
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')

def requestingAPI(coin):
    try:
        req = requests.get('https://economia.awesomeapi.com.br/last/' + coin)
        dicionario = json.loads(req.text)
        return gettingQuote(dicionario[coin+'BRL'])
    except:
        print('Erro na requisição!')
        return req
    
def gettingQuote(coin):
    coinName = coin['name'].split('/')
    valueCoin = float(coin['ask'])
    whenChecked = coin['create_date']
    return coinName[0].lower(), valueCoin, whenChecked

def printCoin(coinName, valueCoin, whenChecked):
    print(f'\nAqui está a ultima cotação de \033[35m{coinName}\033[0m encontrada:')
    print('\033[35m', 8*'-', f'{round(valueCoin, 2)} REAIS', 8*'-', '\033[0m')
    print(f'\n1 {coinName} hoje - {whenChecked}.')
    input('\nEnter continua...')

def convertCoins(coin, mode):
    coinName, valueCoin, whenChecked = requestingAPI(coin)
    while True:
        if mode == 'toBRL':
            convertValue = input(f'\nInsira aqui o valor \033[31m(sem . separando nos números)\033[0m em \033[35m{coinName}\033[0m que você deseja converter para reais: ').strip()
        else:
            convertValue = input(f'\nInsira aqui o valor \033[31m(sem . separando nos números)\033[0m em \033[35mREAIS\033[0m que você deseja converter para {coinName}: ').strip()
        
        try:
            if convertValue.find(',') != -1:
                convertValue = convertValue.replace(',', '.')
            convertValue = float(convertValue)
            if mode == 'toBRL':
                valueConverted = convertValue * valueCoin
                print(f'\nO valor de \033[35m{round(convertValue, 2)} {coinName}\033[0m em reais é:')
                print('\033[35m', 8*'-', f'{round(valueConverted, 2)} REAIS', 8*'-', '\033[0m')
            else:
                valueConverted = convertValue / valueCoin
                print(f'\nO valor de \033[35m{round(convertValue, 2)} reais\033[0m em {coinName} é:')
                print('\033[35m', 8*'-', f'{round(valueConverted, 2)} {coinName}', 8*'-', '\033[0m')

            print(f'\033[31m*Valor de acordo com a cotação de {whenChecked}\033[0m')
            input('\nEnter continua...')
            break

        except:
            print('\033[31mValor inserido inválido!\033[0m\n Tente novamente.')
            clearTerminal()
            continue