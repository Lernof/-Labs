from typing import List
from dataclasses import dataclass
from enum import Enum

class WalletType(Enum):
    KZT = 'KZT'
    USD = 'USD'
    RUB = 'RUB'
    EUR = 'EUR'
    
@dataclass
class Wallet:
    wallet_type: WalletType
    __cash_amount: int = 0
    #getter
    @property
    def cash_amount(self):
        return self.__cash_amount
    #setter
    @cash_amount.setter
    def cash_amount(self, amount:int):
        if amount >= 0:
            self.__cash_amount = amount
        else:
            print('Invalid amount of money')

class User:

    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname
        self.wallets: List[Wallet] = []
    
    def create_wallet(self, wallet_type: WalletType):
        self.wallets.append(Wallet(wallet_type=wallet_type))

    def search_for_wallet(self, wallet_type: WalletType):
        return next((w for w in self.wallets if w.wallet_type == wallet_type), None)

    def addToBankAccount(self, amount: int, wallet_type: WalletType):
        wallet = self.search_for_wallet(wallet_type=wallet_type)
        wallet.cash_amount += amount

    def substractFromBankAccount(self, amount: int, wallet_type: WalletType):
        wallet: Wallet = self.search_for_wallet(wallet_type=wallet_type)
        if amount > wallet.cash_amount:
            print('You don\'t have such money')
            return
        wallet.cash_amount -= amount

    def __del__(self):
        print('Object destroyed')