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
    usd_coefficient: float
    __cash_amount: float = 0
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
    
    def create_wallet(self, wallet_type: WalletType, usd_coefficient: float):
        self.wallets.append(Wallet(wallet_type=wallet_type, usd_coefficient=usd_coefficient))

    def search_for_wallet(self, wallet_type: WalletType):
        return next((w for w in self.wallets if w.wallet_type == wallet_type), None)

    def money_conversion(self, wallet_type1: WalletType, wallet_type2: WalletType, amount: float):
        first_wallet = self.search_for_wallet(wallet_type=wallet_type1)
        second_wallet = self.search_for_wallet(wallet_type=wallet_type2)
        conversion_money = (amount * first_wallet.usd_coefficient) / second_wallet.usd_coefficient

        self.substractFromBankAccount(wallet_type=wallet_type1,amount=amount)
        self.addToBankAccount(wallet_type=wallet_type2, amount=conversion_money)


    def addToBankAccount(self, amount: float, wallet_type: WalletType):
        wallet = self.search_for_wallet(wallet_type=wallet_type)
        wallet.cash_amount += amount

    def substractFromBankAccount(self, amount: float, wallet_type: WalletType):
        wallet: Wallet = self.search_for_wallet(wallet_type=wallet_type)
        if amount > wallet.cash_amount:
            print('You don\'t have such money')
            return
        wallet.cash_amount -= amount

    def __del__(self):
        print('Object destroyed')