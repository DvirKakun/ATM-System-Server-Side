from database import accounts

def Get_Balance(account_number):
    if account_number not in accounts:
        raise ValueError("Account not found")

    return accounts[account_number]

def Withdraw(account_number, amount):
    if account_number not in accounts:
        raise ValueError("Account not found")

    if amount > accounts[account_number]:
        raise ValueError("Insufficient funds")

    if amount <= 0:
        raise ValueError("Withdraw amount must be positive")

    accounts[account_number] -= amount

    return accounts[account_number]

def Deposite(account_number, amount):
    if account_number not in accounts:
        raise ValueError("Account not found")

    if amount <= 0:
        raise ValueError("Deposit amount must be positive")

    accounts[account_number] += amount

    return accounts[account_number]