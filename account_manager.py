from account import Account
class AccountManager:
    """
       Manages a collection of accounts, allowing for account creation, withdrawals, deposits, and balance retrieval.

       Attributes:
           _accounts (dict): A dictionary that stores accounts, keyed by account number.
           _next_account_number (int): The next unique account number to be assigned.

       Methods:
           Add_Account(balance=0):
               Creates and adds a new account to the system with a given balance.

           _get_account(account_number):
               Retrieves an account by its account number, raising an error if not found.

           Withdraw(account_number, amount):
               Withdraws a specified amount from the given account, if sufficient funds are available.

           Deposit(account_number, amount):
               Deposits a specified amount into the given account.

           Get_Balance(account_number):
               Retrieves the current balance of the specified account.
       """
    def __init__(self):
        """
        Initializes the AccountManager with an empty set of accounts and sets the next account number to 1.
        """
        self._accounts = {}
        self._next_account_number = 1

    def Add_Account(self, balance = 0):
        """
        Creates a new account with the specified balance and adds it to the account database.

        Args:
            balance (float, optional): The initial balance of the new account. Defaults to 0.

        Returns:
            int: The unique account number assigned to the new account.
        """
        account_number = self._next_account_number
        self._next_account_number += 1
        self._accounts[account_number] = Account(account_number, balance)

        return account_number

    def _get_account(self, account_number):
        """
        Retrieves an account by its account number.

        Args:
            account_number (int): The account number to retrieve.

        Raises:
            ValueError: If the account number does not exist in the database.

        Returns:
            Account: The account object associated with the given account number.
        """

        if account_number not in self._accounts:
            raise ValueError("Account not found")

        return self._accounts[account_number]

    def Withdraw(self, account_number, amount):
        """
        Withdraws a specified amount from the given account.

        Args:
            account_number (int): The account number to withdraw from.
            amount (float): The amount to withdraw. Must be positive and not exceed the balance.

        Returns:
            float: The new balance of the account after the withdrawal.
        """

        current_account = self._get_account(account_number)

        return current_account.Withdraw(amount)

    def Deposite(self, account_number, amount):
        """
        Deposits a specified amount into the given account.

        Args:
            account_number (int): The account number to deposit into.
            amount (float): The amount to deposit. Must be positive.

        Returns:
            float: The new balance of the account after the deposit.
        """

        current_account = self._get_account(account_number)

        return current_account.Deposite(amount)

    def Get_Balance(self, account_number):
        """
        Retrieves the current balance of the specified account.

        Args:
            account_number (int): The account number to check the balance of.

        Returns:
            float: The current balance of the specified account.
        """

        current_account = self._get_account(account_number)

        return current_account.Get_Balance()
