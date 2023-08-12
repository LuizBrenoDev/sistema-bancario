# Version 2.0.0
# Author: Luiz Breno (LuizBrenoDev)

import random
from datetime import datetime


def get_age(birth_date: str):
    fields = birth_date.split('/')
    year = fields[2]

    spliter = str(datetime.now()).split(' ')
    date = spliter[0]
    fields = date.split('-')
    actual_year = fields[0]

    return int(actual_year) - int(year)


class Client:
    def __init__(self, id: int, name: str, birth_date: str, cpf: int, address: str, transactions: list, password: str):
        self.id = id
        self.name = name
        self.birth_date = birth_date
        self.cpf = cpf
        self.address = address
        self.transactions = transactions
        self.password = password


class Account:
    def __init__(self, agency_number: str, account_number: int, income: float, client: Client):
        self.agency_number = agency_number
        self.account_number = account_number
        self.income = income
        self.client = client


class Transaction:
    def __init__(self, name: str, value: float, date: str):
        self.name = name
        self.value = value
        self.date = date


tester1 = Client(432, 'tester', '13/04/1976', 332415144, 'Praça alves, 13 - Margarida - São Paulo/SP', [], 'test1')
tester2 = Client(332, 'tester2', '20/07/1988', 666673352, 'Praça pedrão, 2 - Pedras Novas - Rio de Janeiro/RJ',
                 [], 'test2')
clients = [tester1, tester2]

acc = Account('001', 1, 1000.0, tester1)
acc2 = Account('001', 2, 2000.0, tester2)

accounts = [acc, acc2]


def account(account: Account):
    print(f'Welcome for your account sir {account.client.name}')
    while True:
        print('Choose one operation: ')
        print(f'''
         Conta de {account.client.name}                                 
         _________________________________________________________
        | Operations:                                             |
        | Pressione "1" para transferir                           |
        | Pressione "2" para depositar                            |
        | Pressione "3" para sacar                                |
        | Pressione "4" para verificar o saldo                    |
        | Pressione "5" para visualizar o seu extrato             |
        | Pressione "0" para voltar para a tela principal         |
        |                                                         |
        |                                                         |
        + ------------------------------------------------------- +
        ''')
        option = input('Reply: ')
        print('')

        def deposit(deposit_value: float, /):
            account.income += value
            account.client.transactions.append(Transaction(f'Depósito de {deposit_value} em {datetime.now()}',
                                                           value, str(datetime.now())))
            print(f'Seu saldo atual é {account.income}')

        def extract():
            for transaction in account.client.transactions:
                print(transaction.name)

        def withdraw(value_withdraw: float):
            if value_withdraw < account.income:
                account.income -= value
            elif value_withdraw > account.income:
                print('ERRO: VALOR A SER SACADO É MAIOR QUE O SALDO')

        def transfer(*, receiver_id: int, value: float):
            if value <= account.income:
                for other_account in accounts:
                    if other_account.client.id == receiver_id:
                        withdraw(value)
                        other_account.income += value
                        account.client.transactions.append(
                            Transaction(
                                f'Transferência de {value} reais para {other_account.client.name} em {datetime.now()}',
                                value, str(datetime.now())))
                        print(f'{value} foi transferido para {other_account.client.name}')
                    elif other_account.client.id != receiver_id:
                        print('')
            elif value > account.income:
                print('ERRO: VALOR A SER SACADO É MAIOR QUE O SALDO')

        match option:
            case '1':
                id = int(input('Insira o id para quem você deseja transferir: '))
                value = float(input('Insira o valor a ser tranferido: '))
                transfer(receiver_id=id, value=value)

            case '2':
                value = float(input('Enter the value to deposit: '))
                deposit(value)

            case '3':
                value = float(input('Insira o valor que deseja sacar: '))
                withdraw(value)
            case '4':
                print('SALDO'.center(30, '-'))
                print(f'Seu saldo atual é {account.income}')
                print('SALDO'.center(30, '-'))
            case '5':
                print('Extrato: ')
                extract()
            case '0':
                print('Exiting for main view...')
                break
            case _:
                pass


def main():
    while True:
        menu_principal = '''
\033[33mChoose one of this options:
[1] Login
[2] Enter a existing account
[3] Create a client
[4] Create Account for a existing client
[0] Exit for application
    
Insira um comando válido: '''
        option = input(menu_principal)

        match option:
            case '1':
                id = input('Insert your client id: ')
                password = input('Insert your client password: ')

                for acc in accounts:
                    if acc.client.password == password and acc.client.id == int(id):
                        print('Exactly')
                        account(acc)
                    elif acc.client.password != password:
                        print('')
                    elif acc.client.id != int(id):
                        print('')

            case '2':
                id = input('Insira o seu id de usuário: ')
                password = input('Insira a sua senha: ')
                acc_num = input('Insira o número da conta: ')

                for acc in accounts:
                    if acc.client.id == int(id) and acc.client.password == password and acc.account_number == int(acc_num):
                        account(acc)
                    elif acc.client.id != int(id):
                        print('ERROR: Id do usuário incorreto')
                    elif acc.client.password != password:
                        print('ERROR: A senha está incorreta')
                    elif acc.account_number != int(acc_num):
                        print('ERROR: O número da conta está incorreto')

            case '3':
                name = input('Insira o seu nome completo: ')
                birth_date = input('Insira a sua data de nascimento: ')
                cpf = int(input('Insira o seu CPF: '))
                logradouro = input('Insira o seu logradouro: ')
                house_number = input('Insira o número da sua casa: ')
                bairro = input('Insira o nome do seu bairro: ')
                city = input('Insira  o nome da sua cidade: ')
                state = input('Insira o nome do seu estado: ')
                password = input('Insira uma senha: ')

                address = f'{logradouro}, {house_number} - {bairro} - {city}/{state}'
                id = random.randint(0, 1000)

                cont = 0
                for client in clients:
                    if client.cpf == cpf:
                        cont += 1
                    elif client.cpf != cpf:
                        print(' ')

                if cont >= 1:
                    print('ERRO: CPF já existe no sistema')
                elif get_age(birth_date) < 18:
                    print('ERRO: IDADE MENOR QUE 18 ANOS')
                elif cont <= 0 and get_age(birth_date) > 18:
                    new_client = Client(id, name, birth_date, cpf, address, [], password)
                    clients.append(new_client)
                    print(f'Novo cliente salvo! O seu id é {id}')
            case '4':
                id = input('Insert your client id: ')
                password = input('Insert your client password: ')

                for client in clients:
                    if client.password == password and client.id == int(id):
                        print('Exactly')
                        new_account = Account('001', len(accounts) + 1, 0.0, client)
                        print(f'Account Created!! id = {new_account.account_number}')
                        account(new_account)
                        accounts.append(new_account)
                    elif client.password != password:
                        print('')
                    elif client.id != int(id):
                        print('')

            case '0':
                print('fatal: Encerrando sessão....')
                break
            case _:
                print('Comando errado, por favor revise ou contate um administrador... ')
                pass


print('Welcome for my bank system!!')
main()
