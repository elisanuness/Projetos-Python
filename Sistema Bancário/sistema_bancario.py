import os

saldo = 0
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUES = 500.

menu = f'''
    Bem vindo ao Banco!
    --------------------------------    
    Selecione uma das opções abaixo:
    [1] Depósito
    [2] Saque
    [3] Extrato
    [0] Sair 
    --------------------------------
      
    => '''

while True:
    opcao = int(input(menu))

    if opcao == 1:
        
        os.system('cls')
        deposito = f'''
        DEPÓSITO ---------------------------------
        Atenção: Insira um valor positivo

        Saldo em conta: {saldo: .2f}
        Insira abaixo o valor de depósito
        => '''
        
        valor = float(input(deposito))

        if valor < 0 :
            print('''
                Valor inválido!
                Por favor, digite um valor positivo!
                ''')
        else:
            extrato +=f'Depósito ---------------------------------------- R${valor}\n'
            saldo += valor 
            print(f'\n\tDepósito de {valor: .2f} concluído com sucesso!\n')

    elif opcao == 2:
       
        os.system('cls')
        saque = f'''
        SAQUE ---------------------------------
        Atenção: Insira um valor positivo.
                Limite de valor por saque = R$ 500.00
                São permitidos apenas 3 saques por dia.

        Saldo em conta: {saldo: .2f}
        Insira abaixo o valor do saque
        => '''

        valor = float(input(saque))

        if valor < 0:
            print('''
                Valor inválido!
                Por favor, digite um valor positivo!
                ''')
        elif valor > saldo :
            print('''
            Você não possui saldo para este saque!
            Por favor, digite um valor válido!
            ''')
        elif valor > LIMITE_VALOR_SAQUES:
            print('''
                Valor inválido!
                Por favor, digite um valor menor que R$ 500.00!
                ''')
        elif numero_saques >= LIMITE_SAQUES:
            print('''
                Você já realizou todos os saques permitidos por hoje!
                Por favor, retorne amanhã!
                ''')
        else:
            extrato += f'Saque ------------------------------------------- R${valor}\n'
            saldo -= valor
            numero_saques += 1
            print(f'\n\tSaque de {valor: .2f} concluído com sucesso!\n')
        
    elif opcao == 3:
        
        os.system('cls')
        print('-------------------------- EXTRATO --------------------------\n')
        if not extrato :
            print('Não foram realizadas transações!')
        else: 
            print(f'{extrato}')
        print(f'Saldo atual da conta: R${saldo :.2f}\n')

    elif opcao == 0 :
        os.system('cls')
        print('Saindo...')
        break

    else :
        os.system('cls')
        print('Opção Inválida! Tente novamente!')


    




