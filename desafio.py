from time import sleep

saldo = numero_saques = 0
limite = 500
extrato = ''
LIMITE_SAQUES = 3

while True:
    print('''
----------------------------------------
                \033[4mBANCO \033[1mDIO\033[m
    [\033[32m1\033[m] Depositar
    [\033[32m2\033[m] Sacar
    [\033[32m3\033[m] Extrato
    [\033[31m0\033[m] \033[1;31mSair\033[m
----------------------------------------
    ''')

    opção = int(input('Digite uma opção: \033[32m'))
    print('\033[m',end='')

    if opção == 1: # Depósito;
        depósito = float(input('Digite um valor de depósito: R$ \033[32m'))
        print('\033[m',end='')

        if depósito > 0: # Proibir digitação de números nulos (0) ou negativos;
            saldo += depósito
            extrato += f'\033[32mDepósito\033[m de R$ {depósito:.2f}\n'
            print(f'O valor de R$ {depósito:.2f} foi adicionado ao seu saldo.')

        else:
            print(f'\033[31mOperação falhou!\033[m Os valores informados estão incorretos.')

    elif opção == 2: # Saque;
            saque = float(input('Digite um valor para sacar: R$ \033[32m'))
            print('\033[m',end='')    

            excedeu_saldo = saque > saldo

            excedeu_limite = saque > limite

            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print('\033[31mOperação falhou!\033[m Você não tem saldo suficiente.')
            
            elif excedeu_limite:
                print('\033[31mOperação falhou!\033[m O valor do saque excede o limite.')

            elif excedeu_saques:
                print('\033[31mOperação falhou!\033[m Número máximo de saques excedido.')

            elif saque > 0: 
                saldo -= saque
                extrato += f'\033[33mSaque\033[m de: R$ {saque:.2f}\n'
                numero_saques += 1
                print(f'O valor de R$ {saque:.2f} foi sacado de sua conta.')

            else:
                print('\033[31mOperação falhou!\033[m O valor informado é inválido!')

    elif opção == 3: # Extrato;
        print(f'EXTRATO BANCÁRIO'.center(50,'-'))
        print(f'Não houve movimentações em sua conta.' if not extrato else f'Movimentações em sua conta: \n{extrato}')
        print(f'Seu saldo atual é: R$ \033[32m{saldo:.2f}\033[m')
        print(f''.center(50,'-'))
    elif opção == 0: # Encerrar programa;
        print('\nEncerrando programa...\n')
        sleep(1) # Dar a impressão que a máquina está pensando;
        break

    else:
        print('\033[31mOperação inválida!\033[m Por favor, selecione uma opção entre 0 e 3.')
