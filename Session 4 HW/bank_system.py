from bank_account import BankAccounts


class BankSystem:
    def __init__(self):
        self.bank_accounts = []

    def start(self):
        pass

    def create_account(self, acc_num, acc_name):
        ac = BankAccounts(acc_num, acc_name, 0)
        self.bank_accounts.append(ac)

    def search(self, num):
        for ac in self.bank_accounts:
            if ac.acc_num == num:
                ac.print_info()

    def modify(self):
        pass

    def print_all_account(self):
        for ac in self.bank_accounts:
            ac.print_info()


