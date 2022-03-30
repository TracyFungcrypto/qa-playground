class BankAccounts:
    def __init__(self, acc_num, acc_name, acc_balance):
        self.acc_num = acc_num
        self.acc_name = acc_name
        self.acc_balance = acc_balance

    def deposit(self, amount):
        self.acc_balance += amount

    def withdraw(self, amount):
        self.acc_balance -= amount

    def print_info(self):
        print(f'{self.acc_name} : {self.acc_num} : {self.acc_balance}')

