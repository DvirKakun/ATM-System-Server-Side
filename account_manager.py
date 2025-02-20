from account import Account
class AccountManager:
    def __init__(self):
        self._accounts = {}
        self._next_account_number = 1

    def Add_Account(self, balance = 0): #Add new account to the database keeping unique account numbers
        account_number = self._next_account_number
        self._next_account_number += 1
        self._accounts[account_number] = Account(account_number, balance)

        return account_number

    def _get_account(self, account_number):
        if account_number not in self._accounts:
            raise ValueError("Account not found")

        return self._accounts[account_number]

    def Withdraw(self, account_number, amount):
        current_account = self._get_account(account_number)

        return current_account.Withdraw(amount)

    def Deposite(self, account_number, amount):
        current_account = self._get_account(account_number)

        return current_account.Deposite(amount)

    def Get_Balance(self, account_number):
        current_account = self._get_account(account_number)

        return current_account.Get_Balance()
