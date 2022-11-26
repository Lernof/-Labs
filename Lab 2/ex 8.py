bank_account = 0
def addToBankAccount(x: float) -> None:
    global bank_account
    bank_account += x
    print(f'money: {bank_account}')

def substractFromBankAccount(x: float) -> None:
    global bank_account
    bank_account -= x
    if bank_account < 0:
        print('You dont have such money')
    else: print(f'money: {bank_account}')

def moneyConversion(x: float, currency1: str, currency2: str) -> None:
    global bank_account
    if x <= bank_account:
        if currency1.lower() == "usd":
            print(f'{x} USD equal to {x * 470} KZT')
                  
        elif currency1.lower() == "kzt":
            print(f'{x} KZT equal to {x / 470} USD')
                  
        else: print('incorrect currency')
    else: print('Incorrect bank account value')
