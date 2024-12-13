"""
    Design a Bank.

    Services
        Customers can open accounts and deposit/withdraw money
        We are only concerned with transactions that take place within a physical location (i.e. through a bank teller)
    Tellers
        Tellers can perform transactions on behalf of customers
        Every transaction is recorded and associated with the Teller and Customer
    Headquarters
        Each branch location will send money to a central location (i.e. the bank's headquarters) at the end of the day
        We don't need to worry about the transporation details
"""

from abc import ABC, abstractmethod

# A Transaction will be tied to a customer and a teller. 
# We will have a get_transaction_description method that will be implemented by the child classes.
# This design follows the Open-Closed Principle since we can add new transaction types without modifying the Transaction class.
class Transaction(ABC):
    def __init__(self, customerId, tellerId):
        self._customerId = customerId
        self._tellerId = tellerId

    def get_customer_id(self):
        return self._customerId

    def get_teller_id(self):
        return self._tellerId
    
    @abstractmethod
    def get_transaction_description(self):
        pass


# The three transaction types will inherit from Transaction and implement the get_transaction_description method
class Deposit(Transaction):
    def __init__(self, customerId, tellerId, amount):
        super().__init__(customerId, tellerId)
        self._amount = amount

    def get_transaction_description(self):
        return f'Teller {self.get_teller_id()} deposited {self._amount} to account {self.get_customer_id()}'

class Withdrawal(Transaction):
    def __init__(self, customerId, tellerId, amount):
        super().__init__(customerId, tellerId)
        self._amount = amount

    def get_transaction_description(self):
        return f'Teller {self.get_teller_id()} withdrew {self._amount} from account {self.get_customer_id()}'

class OpenAccount(Transaction):
    def __init__(self, customerId, tellerId):
        super().__init__(customerId, tellerId)

    def get_transaction_description(self):
        return f'Teller {self.get_teller_id()} opened account {self.get_customer_id()}'

# A BankTeller primarily exists to associate their ID with each transaction they perform.
class BankTeller:
    def __init__(self, id):
        self._id = id
    
    def get_id(self):
        return self._id

# A BankAccount encapsulates a customer's information, along with their balance.
class BankAccount:
    def __init__(self, customerId, name, balance=0):
        self._customerId = customerId
        self._name = name
        self._balance = balance
    
    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
        self._balance += amount
    
    def withdraw(self, amount):
        self._balance -= amount

# A BankSystem is the central store for all customer accounts and transaction logs, 
# regardless of which BankBranch they take place at.
# For simplicity, we store new accounts in an array, where the ID of the customer account will be the next available index in the array.

class BankSystem:
    def __init__(self, accounts, transactions):
        self._accounts = accounts
        self._transactions = transactions
    
    def get_accounts(self):
        return self._accounts

    def get_account(self, customerId):
        return self._accounts[customerId]

    def get_transactions(self):
        return self._transactions

    def open_account(self, customer_name, tellerId):
        # create account
        customerId = len(self.get_accounts())
        account = BankAccount(customerId, customer_name, 0)
        self._accounts.append(account)

        # log the transaction
        t = OpenAccount(customerId, tellerId)
        self._transactions.append(t)

        return customerId
    
    def deposit(self, customer_id, teller_id, amount):
        # make the deposit
        account = self.get_account(customer_id)
        account.deposit(amount)

        # log the log the transaction
        t = Deposit(customer_id, teller_id, amount)
        self._transactions.append(t)
    
    def withdraw(self, customer_id, teller_id, amount):
        if amount > self.get_account(customer_id).get_balance():
            raise ValueError("Insufficient funds!")

        # make the withdrawal
        account = self.get_account(customer_id)
        account.withdraw(amount)

        # log the transaction
        t = Withdrawal(customer_id, teller_id, amount)
        self._transactions.append(t)

# A BankBranch will be responsible for performing transactions on behalf of customers via available BankTellers.
# We also add methods for cash to be collected from and provided to the BankBranch (via the headquarter Bank).
import random
class BankBranch:
    def __init__(self, address, cash_on_hand, bank_system):
        self._address = address
        self._cash_on_hand = cash_on_hand
        self._bank_system = bank_system
        self._tellers = []

    def add_teller(self, teller):
        self._tellers.append(teller)
    
    def _get_available_teller(self):
        index = round(random.random() * (len(self._tellers) - 1))
        return self._tellers[index].get_id()
    
    def open_account(self, customer_name):
        if not self._tellers:
            raise ValueError('Branch does not have any tellers')
        tellerId = self._get_available_teller()
        return self._bank_system.open_account(customer_name, tellerId)
    
    def deposit(self, customer_id, amount):
        if not self._tellers:
            raise ValueError('Branch does not have any tellers')
        tellerId = self._get_available_teller()
        self._bank_system.deposit(customer_id, tellerId, amount)
    
    def withdraw(self, customer_id, amount):
        if amount > self._cash_on_hand:
            raise ValueError('Branch does not have enough cash')
        if not self._tellers:
            raise ValueError('Branch does not have any tellers')

        self._cash_on_hand -= amount
        tellerId = self._get_available_teller()
        self._bank_system.withdraw(customer_id, tellerId, amount)
    
    def collect_cash(self, ratio):
        cash_to_collect = round(self._cash_on_hand * ratio)
        self._cash_on_hand -= cash_to_collect
        return cash_to_collect
    
    def provide_cash(self, amount):
        self._cash_on_hand += amount

    
# The headquarter Bank will be responsible for managing all BankBranches, as well as collecting cash from each branch.
# For convenience, we also add a method to print all transactions that have taken place.
class Bank:
    def __init__(self, bank_branches, bank_system, total_cash):
        self._bank_branches = bank_branches
        self._bank_system = bank_system
        self._total_cash = total_cash

    
    def add_branch(self, address, initial_funds):
        branch = BankBranch(address, initial_funds, self._bank_system)
        self._bank_branches.append(branch)
        return branch
    
    def collect_cash(self, ratio):
        for branch in self._bank_branches:
            cash_collected = branch.collect_cash(ratio)
            self._total_cash += cash_collected
        
    def print_transactions(self):
        for t in self._bank_system.get_transactions():
            print(t.get_transaction_description())


# run a simple simulation to demonstrate the functionality of our bank system.

bankSystem = BankSystem([], [])
bank = Bank([], bankSystem, 10000)

branch1 = bank.add_branch('123 Main St', 1000)
branch2 = bank.add_branch('456 Elm St', 1000)

branch1.add_teller(BankTeller(1))
branch1.add_teller(BankTeller(2))
branch2.add_teller(BankTeller(3))
branch2.add_teller(BankTeller(4))

customerId1 = branch1.open_account('John Doe')
customerId2 = branch1.open_account('Bob Smith')
customerId3 = branch2.open_account('Jane Doe')

branch1.deposit(customerId1, 100)
branch1.deposit(customerId2, 200)
branch2.deposit(customerId3, 300)

branch1.withdraw(customerId1, 50)
""" Possible Output:
    Teller 1 opened account 0
    Teller 2 opened account 1
    Teller 3 opened account 2
    Teller 1 deposited 100 to account 0
    Teller 2 deposited 200 to account 1
    Teller 4 deposited 300 to account 2
    Teller 2 withdrew 50 from account 0
"""

bank.print_transactions()
