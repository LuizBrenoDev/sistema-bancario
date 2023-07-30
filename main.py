# Version 1.3.0
# TODO: Conta corrente, visualizar extrato, modularizar as operações.
 
import random
from datetime import datetime

class Client():
    def __init__(self, id: int, name: str, birth_date: str,
                 cpf: int, address: str, income: float, transactions: list, password: str):
        self.id = id
        self.name = name
        self.birth_date = birth_date
        self.cpf = cpf
        self.address = address
        self.income = income
        self.transactions = transactions
        self.password = password

class Transaction():
    def __init__(self, name: str, value: float, date: str):
        self.name = name
        self.value = value
        self.date = date


tester1 = Client(432, 'tester', '13/04/1976', 332415144, 'Praça alves, 13 - Margarida - São Paulo/SP', 1000.0, [Transaction('Deposit of 1000', 1000.0, '30/06/2023')], 'test')
tester2 =  Client(332, 'tester2', '20/07/1988', 666673352, 'Praça pedrão, 2 - Pedras Novas - Rio de Janeiro/RJ', 2000.0, [Transaction('Deposit', 2000.0, '22/05/2023')], 'test2')
clients = [tester1, tester2]

def account(client: Client):
    print(f'Welcome for your account sir {client.name}')
    while True:
        print('Choose one operation: ')
        print(f'''
     Conta de {client.name}                                 
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

        def transfer(*, receiver_id: int, value: float):
            for other_client in clients:
                    if other_client.id == receiver_id:
                        client.income -= value
                        other_client.income += value
                        client.transactions.append(Transaction('Tranfer', value, datetime.now()))
                        print(f'{value} foi transferido para {other_client.name}')
                    elif other_client.id != receiver_id:
                        print('')

        def deposit(value: float, /):
            client.income += value
            client.transactions.append(Transaction('Deposit', value, datetime.now()))
            print(f'Seu saldo atual é {client.income}')
            

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
                client.income -= value
            case '4':
                print('SALDO'.center(30, '-'))
                print(f'Seu saldo atual é {client.income}')
                print('SALDO'.center(30, '-'))
            case '5':
                print('Extrato: ')
                for transaction in client.transactions:
                    print(transaction.name)
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
[2] Create Account
[0] Exit for application
    
Insira um comando válido: '''  
        option = input(menu_principal)

        match option:
            case '1':
                id = input('Insert your id: ')
                password = input('Insert your password: ')
                
                for client in clients:
                    if client.password == password and client.id == int(id):
                        print('Exactly')
                        account(client)
                    elif client.password != password:
                        print('')
                    elif client.id != int(id):
                        print('')


            case '2':
                name = input('Insira o seu nome completo: ')
                birth_date = input('Insira a sua data de nascimento: ')
                cpf = input('Insira o seu CPF: ')
                logradouro = input('Insira o seu logradouro: ')
                house_number = input('Insira o número da sua casa: ')
                bairro = input('Insira o nome do seu bairro: ')
                city = input('Insira  o nome da sua cidade: ') 
                state = input('Insira o nome do seu estado: ')
                password = input('Insira uma senha para a sua conta: ')

                address = f'{logradouro}, {house_number} - {bairro} - {city}/{state}'
                id = random.randint(0, 1000)

                new_client = Client(id, name, birth_date, cpf, address, 0.0, password)
                clients.append(new_client)

                print(f'Novo cliente salvo! O seu id é {id}')
            case '0':
                print('fatal: Encerrando sessão....')
                break
            case _:
                print('Comando errado, por favor revise ou contate um administrador... ')
                pass


print('Welcome for my bank system!!')
main()