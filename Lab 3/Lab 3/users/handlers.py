from users.models import WalletType
from users.services import UserServices


class UserHandlers:
    
    services: UserServices

    def __init__(self, services: UserServices):
        self.services = services
    
    def sign_up(self, name: str, surname: str) -> None:
        name = name.strip().lower()
        surname = surname.strip().lower()
        if not self.validate_creds(name=name, surname=surname):
            print('Invalid data')
            return

        self.services.create_user(name=name,surname=surname)

    def sign_in(self, name:str, surname: str) -> None:
        name = name.strip().lower()
        surname = surname.strip().lower()
        if not self.validate_creds(name=name, surname=surname):
            print('Invalid data')
            return None

        return self.services.get_user(name=name,surname=surname)

    def toString(self, name:str, surname:str):
        name = name.strip().lower()
        surname = surname.strip().lower()
        if not self.validate_creds(name=name, surname=surname):
            print('Invalid data')
            return None
        self.services.toString(name=name, surname=surname)

    def create_wallet(self, wallet_type: WalletType, name:str, surname: str):
        name = name.strip().lower()
        surname = surname.strip().lower()
        self.services.create_wallet(wallet_type=wallet_type, name=name, surname=surname)

    def delete_user(self, name:str, surname:str):
        name = name.strip().lower()
        surname = surname.strip().lower()
        self.services.delete_user(name=name, surname=surname)

    def addToBankAccount(self, name:str, surname:str, amount: int, wallet_type: WalletType):
        name = name.strip().lower()
        surname = surname.strip().lower()
        if amount < 0:
            print('Invalid amount of money')
            return

        self.services.addToBankAccount(name=name,surname=surname,amount=amount, wallet_type=wallet_type)

    def substractFromBankAccount(self, wallet_type: WalletType, name:str, surname: str, amount: int):
        name = name.strip().lower()
        surname = surname.strip().lower()
        if amount < 0:
            print('Invalid amount of money')
            return
        
        self.services.substractFromBankAccount(amount=amount, name=name, surname=surname, wallet_type=wallet_type)

    def money_conversion(self, name:str, surname: str, wallet_type1: WalletType, wallet_type2: WalletType, amount: float):
        if amount < 0:
            print('Invalid amount of money')
            return
        self.services.money_conversion(name=name, surname=surname, wallet_type1=wallet_type1, wallet_type2=wallet_type2, amount=amount)

    def validate_creds(self, name: str, surname: str) -> bool:
        if '$' in name or '$' in surname:
            return False

        return True
        