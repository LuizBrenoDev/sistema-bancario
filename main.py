import random
import account

# Version 0.0.0

class Client :
    def __init__(self, name: str, income: float, password: str):
        self.name = name
        self.income = income
        self.password = password

# Clients for application test
clients = [Client('tester', 2000.0, 'test1'), Client('tester2', 3000.0, 'test2')] 

while True :
    print('''Welcome for my bank system!! 
            [1] Client Login
            [2] Create Account
            [3] Exit\n''')
          
    command = input('-> ')

    match command:
        case '1' : 
            id = int(input('Enter the user id: '))

            password = input('Enter the password: ')
            
            for client in clients:
                if client.password != password:
                    print('Wrong Password. Try Again')
                elif clients.index(client) != id:
                    print('Client not found')
                elif clients.index(client) == id and client.password == password:
                    print(f'\n Welcome for your account sir {client.name}')
                    account.main(client.name, client.income)

            break
                

        case '2' : 
            name = input('Enter the client name: ')
            income = float(input('Enter a initial income: '))
            password = input('Enter the account password: ')
            client = Client(name, income, password)
            clients.append(client)
            
            for client in clients:
                print(client.name)

        case '3':
            print('Closing... ')
            break

        case _:
            print('Invalid Command')
            pass

