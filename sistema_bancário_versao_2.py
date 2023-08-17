def menu():

    opcao = f"""
{'SISTEMA BANCÁRIO':-^50}
[1] SAQUE
[2] DEPÓSITO
[3] EXTRATO
[4] CRIAR USUÁRIO
[5] CRIAR CONTA
[9] SAIR
>>> SUA OPÇÃO: """

    return input(opcao)


def sacar(*, saldo, valor, extrato_saques, limite, numero_saques, LIMITE_SAQUES):

    if valor < 0:
        print('Não é possível sacar valores negativos.')
    elif valor > limite:
        print('Não é possível sacar mais de R$500,00 por vez.')
    elif numero_saques >= LIMITE_SAQUES:
        print('Você já atingiu o número de saques disponíveis por dia.')
    elif valor > saldo:
        print('Você não tem esse valor na conta para sacar.')
    else:
        saldo -= valor
        extrato_saques += f'R$ {valor:.2f}\n'
        numero_saques += 1
        print(f'Você sacou R${valor:.2f}')

    return saldo, extrato_saques, numero_saques


def depositar(saldo, valor, extrato_depositos, /):

    if valor < 0:
        print('Não é possível depositar um valor negativo.')
    else:
        saldo += valor
        extrato_depositos += f'R$ {valor:.2f}\n'
        print(f'Você depositou R${valor:.2f}')

    return saldo, extrato_depositos


def extrato(saldo, /, *, extrato_saques, extrato_depositos):

    print(f'{"EXTRATO":-^50}')
    print('SAQUES')
    print(extrato_saques)
    print('DEPOSITOS:')
    print(extrato_depositos)
    print('SALDO EM CONTA')
    print(f'R$ {saldo:.2f}')


def criar_usuario(cpf, usuarios):

    if cpf in usuarios:
        print('Esse usuário já está cadastrado')
    else:
        usuarios.append(cpf)

    return usuarios


def criar_conta(contas, cpf, agencia, numero_conta, usuarios):

    if cpf not in usuarios:
        print('Esse usuário não está cadastrado')
    else:
        numero_conta += 1
        contas = numero_conta
        print(f'Conta nº{numero_conta} criada com sucesso.')

    return contas, numero_conta


def listar_contas(contas):
    for i in contas:
        print(i)


def main():

    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 400
    limite = 500
    extrato_saques = ''
    extrato_depositos = ''
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 0

    while True:

        menu_opcao = menu()

        if menu_opcao == '1':
            valor = float(input('Qual valor você deseja sacar? R$ '))
            saldo, extrato_saques, numero_saques = sacar(saldo=saldo, valor=valor, extrato_saques=extrato_saques, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)

        elif menu_opcao == '2':
            valor = float(input('Qual valor você deseja depositar? R$ '))
            saldo, extrato_depositos = depositar(saldo, valor, extrato_depositos)

        elif menu_opcao == '3':
            extrato(saldo, extrato_saques=extrato_saques, extrato_depositos=extrato_depositos)

        elif menu_opcao == '4':
            cpf = int(input('Digite seu CPF (Apenas os números): '))
            usuarios = criar_usuario(cpf, usuarios)

        elif menu_opcao == '5':
            cpf = int(input('Digite seu CPF (Apenas os números): '))
            contas, numero_conta = criar_conta(contas, cpf, AGENCIA, numero_conta, usuarios)

        elif menu_opcao == '9':
            break


main()

