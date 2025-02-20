class Account:
    def __init__(self, account_number, balance = 0):
        self._account_number = account_number
        self._balance = balance

    def Get_Balance(self):
        return self._balance

    def Withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient funds")

        self._balance -= amount

        return self._balance

    def Deposite(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self._balance += amount

        return self._balance
