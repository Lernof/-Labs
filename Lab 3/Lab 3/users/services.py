from users.models import WalletType
from users.repositories import UserRepositories

class UserServices:
    
    repositories: UserRepositories

    def __init__(self, repositories: UserRepositories) -> None:
        self.repositories = repositories

    def create_user(self, name: str, surname: str) -> None:
        self.repositories.create_user(name=name, surname=surname)
        self.send_email_verification(f'{name}-{surname}@mail.ru')

    def get_user(self, name: str, surname: str):
        return self.repositories.get_user(name=name,surname=surname)

    def toString(self,name:str,surname:str):
        self.repositories.toString(name=name,surname=surname)

    def delete_user(self, name: str, surname: str):
        self.repositories.delete_user(name=name, surname=surname)

    def create_wallet(self, name: str, surname: str, wallet_type: WalletType):
        self.repositories.create_wallet(name=name,surname=surname,wallet_type=wallet_type)

    def delete_user(self, name:str, surname: str):
        self.repositories.delete_user(name=name, surname=surname)

    def addToBankAccount(self, name:str, surname: str, wallet_type: WalletType, amount: int):
        self.repositories.addToBankAccount(name=name,surname=surname,wallet_type=wallet_type, amount=amount)

    def substractFromBankAccount(self, name: str, surname:str, wallet_type: WalletType, amount: int):
        self.repositories.substractFromBankAccount(name=name, surname=surname, wallet_type=wallet_type, amount=amount)

    def money_conversion(self, name:str, surname:str, amount: float, wallet_type1: WalletType, wallet_type2: WalletType):
        self.repositories.money_confersion(name=name, surname=surname, wallet_type1=wallet_type1, wallet_type2=wallet_type2, amount=amount)

    @staticmethod
    def send_email_verification(email: str) -> None:
        print(f'send email to {email}')