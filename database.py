"""
Script to initialize an AccountManager and create sample accounts.

This script:
1. Creates an instance of `AccountManager` to manage accounts.
2. Adds multiple accounts with different initial balances.

Imports:
    - `AccountManager` from `account_manager`.

Usage:
    Runs with the program to create a set of accounts with predefined balances.
"""

from account_manager import AccountManager

account_manager = AccountManager()

account_manager.Add_Account(1000)
account_manager.Add_Account()
account_manager.Add_Account(2500)
account_manager.Add_Account(5000)
account_manager.Add_Account(15000)
