# Client account interface

def main(client_name: str, client_income: float):
    while True:
        print(f'''Your Account sir {client_name}  
                [1] Income
                [0] Exit
        ''')
        
        command = input('-> ')

        match command:
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case '0':
                print('Closing...')
                break
            case _:
                print('Invalid Command')
                pass

