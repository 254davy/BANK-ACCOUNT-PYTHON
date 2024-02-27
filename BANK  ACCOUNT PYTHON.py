class BankAccount:
    """A class representing a bank account with attributes and methods for deposits, withdrawals, and balance inquiries.

    Attributes:
        account_number: A unique identifier for the account (string).
        balance: The current balance of the account (float).
        date_opened: The date the account was opened (string).
        customer_name: The name of the account owner (string).

    Methods:
        deposit(amount): Deposits the specified amount into the account.
        withdraw(amount): Withdraws the specified amount from the account, if sufficient funds are available.
        get_balance(): Returns the current account balance.
        get_details(): Prints the account details, including account number, customer name, date opened, and balance.
    """

    def __init__(self, account_number, customer_name, balance=0.0, date_opened=None):
        """
        Initializes a new BankAccount object.

        Args:
            account_number: The account number (string).
            customer_name: The name of the account owner (string).
            balance: The initial balance (float, defaults to 0.0).
            date_opened: The date the account was opened (string, defaults to None).
        """
        self.account_number = account_number
        self.balance = balance
        self.customer_name = customer_name
        self.date_opened = date_opened if date_opened else strftime("%Y-%m-%d")  # Use current date if not provided

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.

        Args:
            amount: The amount to deposit (float).

        Returns:
            The new account balance (float).
        """
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account, if sufficient funds are available.

        Args:
            amount: The amount to withdraw (float).

        Returns:
            The new account balance (float) if successful, otherwise None.
        """
        if amount > self.balance:
            print("Insufficient funds.")
            return None

        self.balance -= amount
        return self.balance

    def get_balance(self):
        """
        Returns the current account balance.

        Returns:
            The current account balance (float).
        """
        return self.balance

    def get_details(self):
        """
        Prints the account details, including account number, customer name, date opened, and balance.
        """
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Date Opened: {self.date_opened}")
        print(f"Balance: ${self.balance:.2f}")  # Format balance to two decimal places
