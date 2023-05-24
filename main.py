import os
import request
os.system('cls' if os.name == 'nt' else 'clear')

menu = ['Ver cotação atual', 'Fazer conversão Dólar -> Real', 'Fazer conversão Real -> Dólar', 'Sair']

def exitingProgram():
    print('\033[32m\nObrigado por utilizar meu programa!\033[0m\nVolte sempre que estiver pensando naquela viajem viagem economica ou aquele produto importado 😁✌️')
    exit()

print('\033[35mConversor monetário!\033[0m\n')

while True:
    print('O que você deseja fazer? ')
    for index, item in enumerate(menu):
        print(f'[{index + 1}] {item}.')
    mode = input('>> ')

    if not mode.isdigit() or int(mode)-1 >= len(menu) or int(mode)-1 < 0:
        print('Você inseriu algo inválido!\n Tente novamente.')
        request.clearTerminal()

    else:
        match(mode):
            case '1': 
                coinName, valueCoin, whenChecked = request.requestingAPI('USD')
                request.printCoin(coinName, valueCoin, whenChecked)
            case '2': request.convertCoins('USD', 'toBRL')
            case '3': request.convertCoins('USD', '')
            case '4': exitingProgram()
        request.clearTerminal()