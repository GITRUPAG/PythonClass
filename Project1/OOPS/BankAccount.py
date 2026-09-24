class BankAccount:

    def __init__(self, balance):
        # self.balance = balance
        self.__balance = balance  # Private attribute - name mangling

    def get_balance(self):
        return self.__balance
    def set_balance(self, balance):
        self.__balance = balance

    def withdraw(self, amount):
        if(amount < self.__balance):
            self.__balance = self.__balance - amount

            print("Amount Withdrawed!!!!", amount)
            print("Balance : ", self.__balance)
        else:
            print("Not enough Money!!!")




account = BankAccount(8000)
# account.balance =50000

# print(account.balance) # raises attribute error

print(account.get_balance())

account.set_balance(1000)

print(account.get_balance())

account.withdraw(500)

