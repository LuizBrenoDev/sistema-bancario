import random

class Client():
    def __init__(self, id: int, name: str, income: float, password: str):
        self.id = id
        self.name = name
        self.income = income
        self.password = password
    

def account(client: Client):
    print(f'Welcome for your account sir {client.name}')
    while True:
        print('Choose one operation: ')
        print(f'''
     _________________________________________________________
    |Account of {client.name} | Income: {client.income}       |
    |_________________________________________________________|
    | Operations:                                             |
    | Press "1" for transfer                                  |
    | Press "2" for deposit                                   |
    | Press "0" for exit to main view                         |
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
                value = input('Enter the value to deposit: ')
                client.income = client.income + float(value)
                print(f'Your actual income is {client.income}')
            case '3':
                pass
            case '0':
                print('Exiting for main view...')
                break
            case _:
                pass

    

def main():
    tester1 = Client(432, 'tester', 2000.0, 'test')
    tester2 =  Client(332, 'tester2', 1000.0, 'test2')
    clients = [tester1, tester2]
    
    while True:
        print('''
    Choose one of this options:
    [1] Login
    [2] Create Account
    [0] Exit for application
        ''')  
        option = input('-> ')

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
                password = input('Insert a password for your account: ')
                id = random.randint(0, 1000)

                new_client = Client(id, name, 0.0, password)
                clients.append(new_client)
                print(f'New client created! id: {id}')
            case '0':
                print('Closing....')
                break
            case _:
                print('Invalid input... ')
                pass


print('Welcome for my bank system!!')
main()