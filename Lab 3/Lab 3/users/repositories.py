from typing import List

from users.models import User, WalletType

class UserRepositories:
    users: List[User] = []
    
    def create_user(self, name: str, surname: str):

        user = User(name=name,surname=surname)
        self.users.append(user)

    def create_wallet(self, wallet_type: WalletType, name: str, surname: str):
        user = self.get_user(name=name,surname=surname)
        if not self.validate_wallet_type(wallet_type=wallet_type, user=user):
            return

        usd_coefficient: float = 0

        match wallet_type.name:
            case wallet_type.name if wallet_type.name == 'USD':
                usd_coefficient = 1
            case wallet_type.name if wallet_type.name == 'KZT':
                usd_coefficient = 0.002
            case wallet_type.name if wallet_type.name == 'EUR':
                usd_coefficient = 1.05
            case wallet_type.name if wallet_type.name == 'RUB':
                usd_coefficient = 0.016

        user.create_wallet(wallet_type=wallet_type, usd_coefficient=usd_coefficient)
        print(f'wallet with wallet type {wallet_type} was added to the \'{name}-{surname}\' account')

    def toString(self, name:str, surname:str):
        user = self.get_user(name=name,surname=surname)
        if not user:
            return
        print(f'{user.name=}\t{user.surname=}')
        print('Your wallets: ')
        for i in user.wallets:
            print(f'Wallet type: {i.wallet_type.name}, cash amount: {i.cash_amount}, usd_coefficient: {i.usd_coefficient}')


    def delete_user(self, name:str, surname: str):
        user = self.get_user(name=name, surname=surname)
        if not user:
            return

        del self.users[self.users.index(user)]

    def addToBankAccount(self, wallet_type: WalletType, amount: int, name:str, surname: str):
        user = self.get_user(name=name, surname=surname)
        if not user:
            return

        if not self.wallet_availability_check(wallet_type=wallet_type,user=user):
            return
        
        user.addToBankAccount(amount=amount, wallet_type=wallet_type)

    def substractFromBankAccount(self, wallet_type: WalletType, amount: int, name:str, surname: str):
        user = self.get_user(name=name, surname=surname)
        if not user:
            return

        if not self.wallet_availability_check(wallet_type=wallet_type,user=user):
            return

        user.substractFromBankAccount(amount=amount, wallet_type=wallet_type)

    def money_confersion(self, wallet_type1: WalletType, wallet_type2: WalletType, amount: float, name: str, surname: str):
        user = self.get_user(name=name,surname=surname)
        user.money_conversion(wallet_type1=wallet_type1, wallet_type2=wallet_type2, amount=amount)

    def get_user(self, name: str, surname: str):
        user = next((w for w in self.users if w.name == name and w.surname == surname), None)
        
        if not user:
            print('User not found')
            return None

        return user

    def validate_wallet_type(self, wallet_type: WalletType, user: User):
        if not user:
            print('User not found')
            return None

        if user.search_for_wallet(wallet_type=wallet_type):
            print('you can\'t have more then one wallet per type of value')
            return None

        return True

    def wallet_availability_check(self, wallet_type:WalletType, user: User):
        wallet = next((w for w in user.wallets if w.wallet_type == wallet_type), None)
        
        if not wallet:
            print('You don\'t have such wallet')
            return False
        return True