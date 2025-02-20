class Account:
    """
     Account class represents a single account.

     Attributes:
         account_number (int): Unique identifier for the account.
         balance (float): The balance of the account.

     Methods:
         Get_Balance(): Returns the current balance of the account.
         Withdraw(amount): Withdraws a specified amount from the account.
         Deposit(amount): Deposits a specified amount into the account.
    """
    def __init__(self, account_number, balance = 0):
        """
        Initializes a new account with a given account number and an optional initial balance.

        Args:
            account_number (int): The unique identifier for the account.
            balance (float, optional): The initial balance of the account. Defaults to 0 if not provided.
        """

        self._account_number = account_number
        self._balance = balance

    def Get_Balance(self):
        """
        Returns the current balance of the account.

        Returns:
            float: The current balance of the account.
        """
        return self._balance

    def Withdraw(self, amount):
        """
        Withdraws a specified amount from the account if there are sufficient funds.

        Args:
            amount (float): The amount to withdraw from the account. Must be positive.

        Returns:
            float: The new balance of the account after the withdrawal.

        Raises:
            ValueError: If the withdrawal amount is not positive or exceeds the available balance.
        """

        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient funds")

        self._balance -= amount

        return self._balance

    def Deposite(self, amount):
        """
            Deposits a specified amount into the account.

            Args:
                amount (float): The amount to deposit into the account. Must be a positive number.

            Returns:
                The new balance of the account after deposit

            Raises:
                ValueError: If the amount is not positive.
            """

        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self._balance += amount

        return self._balance
