class BankAccount:
    def __init__(self, account_number, account_holder, balance) -> None:
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance

    def deposite_money(self, deposite):
        if self.balance>=0:
            self.balance=self.balance + deposite
            return self.balance
        else:
            return -1

    def withdraw_money(self, withdraw):
        if self.balance>=0:
            self.balance=self.balance - withdraw
            return self.balance
        else:
            return -1


Ba=BankAccount(12345678, "Paras", 1000)
balance=Ba.deposite_money(500)
balance=Ba.withdraw_money(2000)

if balance<0:
    print("Wrong balance figure")
else:
    print(f"Balance: {balance}")