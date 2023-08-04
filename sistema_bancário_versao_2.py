def menu():

    global menu_opcao

    menu_opcao = input(
        f'\n{"-" * 60}'
        f'\n{"SISTEMA BANCÁRIO":^60}'
        f'\n{"-" * 60}'
        f'\n[1] SAQUE'
        f'\n[2] DEPOSITO'
        f'\n[3] EXTRATO'
        f'\n[4] CRIAR USUÁRIO'
        f'\n[5] CRIAR CONTA'
        f'\n[6] SAIR'
        f'\nSua opção: '
    )


def saque(*, valor, saldo, limite, numero_saques, LIMITE_SAQUES, extrato_saques):

    global saldo_novo

    if valor > limite:
        print('O valor máximo para saques é de R$500.00.')
    elif valor < 0:
        print('Não é possível sacar um valor negativo.')
    elif numero_saques == LIMITE_SAQUES:
        print('Você já atingiu o limite de três'
              '\nsaques diários.')
    elif valor > saldo:
        print('O seu saldo é inferior ao saque desejado.')
    else:
        numero_saques += 1
        saldo_novo = saldo - valor
        extrato_saques.append(valor)
        print(f'Você sacou R${valor:.2f}.')


def deposito(valor, saldo, extrato_depositos, /):

    global saldo_novo

    if valor < 0:
        print('Não é possivel depositar um valor negativo.')
    else:
        saldo_novo = saldo -+ valor
        extrato_depositos.append(valor)
        print(f'Você depositou R${valor:.2f}.')


def extrato(saldo, /, *, extrato_saques, extrato_depositos):

    print('SAQUES')
    for i in extrato_saques:
        print(f'R$ {i:.2f}')
    print('DEPOSITOS:')
    for i in extrato_depositos:
        print(f'R$ {i:.2f}')
    print('SALDO EM CONTA')
    print(f'R$ {saldo_novo:.2f}')


def criar_usuario(usuarios):

    cpf = input('Digite o CPF: ')
    if cpf in usuarios:
        print('Esse usuário já esta cadastrado')
    else:
        usuarios.append(cpf)


def criar_conta(agencia, numero_conta, usuarios):

    cpf = input('Digite o CPF: ')
    if cpf not in usuarios:
        print('Esse usuário não está cadastrado')
    else:
        conta = numero_conta + 1


def main():

    global numero_conta

    saldo = 1000
    limite = 500
    extrato_saques = []
    extrato_depositos = []
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    numero_conta = 0
    AGENCIA = '0001'

    while True:
        menu()

        if menu_opcao == '1':
            print(f'{"-" * 60}\n{"SAQUE":^60}')
            valor = float(input('Quanto você deseja sacar? R$ '))
            saque(valor=valor, saldo=saldo, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES, extrato_saques=extrato_saques)

        elif menu_opcao == '2':
            print(f'{"-" * 60}\n{"DEPOSITO":^60}')
            valor = float(input('Quanto você deseja depositar? R$ '))
            deposito(valor, saldo, extrato_depositos)

        elif menu_opcao == '3':
            print(f'{"-" * 60}\n{"EXTRATO":^60}')
            extrato(saldo, extrato_saques=extrato_saques, extrato_depositos=extrato_depositos)

        elif menu_opcao == '4':
            criar_usuario(usuarios)

        elif menu_opcao == '5':
            criar_conta(AGENCIA, )

        elif menu_opcao == '6':
            print(f'{"---------- Obrigado pela preferêcia! ----------":^60}')
            break

        else:
            print(f'{"---------- Opção inválida! ----------":^60}')


main()

