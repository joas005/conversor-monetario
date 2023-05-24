import os
import request
os.system('cls' if os.name == 'nt' else 'clear')

# Defining - 
homeMenu = ['Escolher uma moeda', 'Créditos', 'Sair']

possibleCoins = ['Dólar americano', 'Euro', 'Libra esterlina', 'Iene', 'Dólar australiano',
                 'Franco suíço', 'Dólar canadense', 'Rand', 'Yuan', 'Peso argentino']

coinCodes = ['USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CHF', 'CAD', 'ZAR', 'CNY', 'ARS']

# Functions - 
def showCredits():
    print('\n\033[34mObrigado por querer me conhecer\033[0m 😁✌️\nEste programa foi desenvolvido por \033[35m@joas005\033[0m no github, entre lá para conheça um pouco mais sobre mim e meus projetos!')
    input('\nEnter continua...')

def exitingProgram():
    print('\033[32m\nObrigado por utilizar meu programa!\033[0m\nVolte sempre que estiver pensando naquela viajem viagem economica ou aquele produto importado 😁✌️')
    exit()

def choosingCoin():
    while True:
        request.clearTerminal()
        print('Qual moeda você deseja utilizar?\n')
        for index, coin in enumerate(possibleCoins):
            print(f'[{index + 1}] {coin}')

        chosenCoin = input('\n>> ').strip().lower()

        if chosenCoin in possibleCoins:
            print(f'Você escolheu usar a moeda - \033[35m{chosenCoin}\033[0m')
            position = possibleCoins.index(chosenCoin)
            code = coinCodes[position]
            coinName, valueCoin, whenChecked = request.requestingAPI(code)
            operations(code, coinName, valueCoin, whenChecked)

        elif chosenCoin.isdigit() and int(chosenCoin) - 1 <= len(possibleCoins):
            print(f'Você escolheu usar a moeda - \033[35m{possibleCoins[int(chosenCoin)-1]}\033[0m')
            code = coinCodes[int(chosenCoin)-1]
            coinName, valueCoin, whenChecked = request.requestingAPI(code)
            operations(code, coinName, valueCoin, whenChecked)

        else:
            print('Você inseriu algo inválido!\n Tente novamente.')
            request.clearTerminal()
            continue

def operations(coinCode, coinName, valueCoin, whenChecked):
    menuChosenCoin = ['Ver cotação atual', f'Fazer conversão {coinName} -> Real',
                  f'Fazer conversão Real -> {coinName}', 'Trocar de moeda', 'Sair']
    while True:
        request.clearTerminal()
        print('O que você deseja fazer?\n')
        for index, item in enumerate(menuChosenCoin):
            print(f'[{index + 1}] {item}.')
        mode = input('\n>> ').strip()

        if not mode.isdigit() or int(mode)-1 >= len(menuChosenCoin) or int(mode)-1 < 0:
            print('Você inseriu algo inválido!\n Tente novamente.')
            request.clearTerminal()

        else:
            match(mode):
                case '1':
                    request.printCoin(coinName, valueCoin, whenChecked)
                case '2': request.convertCoins(coinCode, 'toBRL')
                case '3': request.convertCoins(coinCode, '')
                case '4': choosingCoin()
                case '5': exitingProgram()

# Main -
print('\033[35mConversor monetário!\033[0m\n')

while True:
    print('O que você deseja fazer?\n')
    for index, item in enumerate(homeMenu):
        print(f'[{index + 1}] {item}.')
    mode = input('>> ').strip()

    if not mode.isdigit() or int(mode)-1 >= len(homeMenu) or int(mode)-1 < 0:
        print('Você inseriu algo inválido!\n Tente novamente.')
        request.clearTerminal()

    else:
        match(mode):
            case '1': choosingCoin()
            case '2': showCredits()
            case '3': exitingProgram()
        request.clearTerminal()