# Version 1.0.0
 
import random

class Client():
    def __init__(self, id: int, name: str, birth_date: str,
                 cpf: int, address: str, income: float, password: str):
        self.id = id
        self.name = name
        self.birth_date = birth_date
        self.cpf = cpf
        self.address = address
        self.income = income
        self.password = password
    

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
    | Pressione "0" para voltar para a tela principal         |
    |                                                         |
    |                                                         |
    + ------------------------------------------------------- +
    ''')
        option = input('Reply: ')
        print('')

        match option:
            case '1':
                print(f'Your income is {client.income}')
            case '2':
                value = float(input('Enter the value to deposit: '))
                client.income += value
                print(f'Your actual income is {client.income}')
            case '3':
                value = float(input('Insira o valor que deseja sacar: '))
                client.income -= value
            case '4':
                print(f'Seu saldo atual é {client.income}')
            case '0':
                print('Exiting for main view...')
                break
            case _:
                pass

    

def main():
    tester1 = Client(432, 'tester', '13/04/1976', 332415144, 'Praça alves, 13 - Margarida - São Paulo/SP', 1000.0, 'test')
    tester2 =  Client(332, 'tester2', '20/07/1988', 666673352, 'Praça pedrão, 2 - Pedras Novas - Rio de Janeiro/RJ', 2000.0, 'test2')
    clients = [tester1, tester2]
    
    while True:
        menu_principal = '''
Choose one of this options:
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
                name = input('Insert your complete name: ')
                birth_date = input('Insira a sua data de nascimento: ')
                cpf = input('Insira o seu CPF: ')
                logradouro = input('Insira o seu logradouro: ')
                numero_casa = input('Insira o número da sua casa: ')
                bairro = input('Insira o nome do seu bairro: ')
                cidade = input('Insira  o nome da sua cidade: ')
                estado = input('Insira o nome do seu estado: ')
                password = input('Insira uma senha para a sua conta: ')

                address = f'{logradouro}, {numero_casa} - {bairro} - {cidade}/{estado}'
                id = random.randint(0, 1000)

                new_client = Client(id, name, birth_date, cpf, address, 0.0, password)
                clients.append(new_client)

                print(f'Novo cliente salvo! O seu id é {id}')
            case '0':
                print('Encerrando sessão....')
                break
            case _:
                print('Comando errado, por favor revise ou contate um admnistrador... ')
                pass


print('Welcome for my bank system!!')
main()