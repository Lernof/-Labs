import sys
from users.handlers import UserHandlers
from users.services import UserServices
from users.repositories import UserRepositories
from users.models import WalletType

def formating_wallet_type(wallet_type: str):

    match wallet_type:
        case 'KZT':
                return WalletType.KZT
        case 'USD':
                return WalletType.USD
        case 'RUB':
                return WalletType.RUB
        case 'EUR':
                return WalletType.EUR
        case _:
                print('Invalid type of value!')
                return None

def index():
    user_repo = UserRepositories()
    user_service = UserServices(repositories=user_repo)
    user_handlers = UserHandlers(services=user_service)
    current_user = None
    while True:

        command = input('\nEnter command or enter q to quit: \n1 - sign up\t2 - sign in\n3 - make wallet\t 4 - delete account\n5 - refill account\t6 - subtract\n7 - Show account information\t8 - money conversion: ')
        
        match command, current_user:
            case '1', current_user:
                name, surname = input('Enter your name and surname: ').split()
                user_handlers.sign_up(name=name, surname=surname)

            case '2', current_user:
                name, surname = input('Enter your creds: ').split()
                current_user = user_handlers.sign_in(name=name, surname=surname)

            case '3', current_user if current_user != None:
                wallet_type = input('Enter type of value: ')
                wallet_type = formating_wallet_type(wallet_type=wallet_type)

                if not wallet_type:
                    sys.exit(1)

                user_handlers.create_wallet(wallet_type=wallet_type, name=name, surname=surname)

            case '4', current_user:
                name, surname = input('Write user you want to delete(Name Surname): ').split()
                user_handlers.delete_user(name=name, surname=surname)

            case '5', current_user if current_user != None:
                wallet_type = input('Enter type of value (USD, RUB, KZT, EUR): ')
                wallet_type = formating_wallet_type(wallet_type=wallet_type)
                
                if not wallet_type:
                    sys.exit(1)

                amount = int(input('Value of refill: '))
                
                user_handlers.addToBankAccount(wallet_type=wallet_type, amount=amount, name=name, surname=surname)

            case '6', current_user if current_user != None:
                wallet_type = input('Enter type of value (USD, RUB, KZT, EUR): ')
                wallet_type = formating_wallet_type(wallet_type=wallet_type)
                
                if not wallet_type:
                    sys.exit(1)

                amount = int(input('Value of substract: '))
                
                user_handlers.substractFromBankAccount(wallet_type=wallet_type, amount=amount, name=name, surname=surname) 

            case '7', current_user:
                name, surname = input('Write user(Name Surname): ').split()
                user_handlers.toString(name=name, surname=surname)

            case '8', current_user if current_user != None:
                wallet_type1, wallet_type2 = input('Enter wallet from ____ to ____ you need to transfer: ').split()
                amount = int(input('Enter amount of money: '))
                wallet_type1 = formating_wallet_type(wallet_type=wallet_type1)
                wallet_type2 = formating_wallet_type(wallet_type=wallet_type2)

                user_handlers.money_conversion(name=name, surname=surname, wallet_type1=wallet_type1, wallet_type2=wallet_type2, amount=amount)

            case _:
                print('Wrong command or you haven\'t signed in')