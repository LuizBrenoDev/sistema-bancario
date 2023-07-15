class Client():
    def __init__(self, name: str, income: float, password: str):
        self.name = name
        self.income = income
        self.password = password


def account(client: Client):
    print(f'Welcome for your account sir {client.name}')

def main():
    clients = [Client('tester', 2000, 'test')]
    
    while True:
        print('Choose one of this options: ')
        print('''
    [1] Login
    [2] Create Account
    [0] Exit
        ''')  
        option = input('-> ')

        match option:
            case '1':
                account(Client('nome', 1000.0, 'teste'))
            case '2':
                pass
            case '0':
                break
            case _:
                print('Closing....')
                pass


print('Welcome for my bank system!!')
main()