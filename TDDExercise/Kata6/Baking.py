from datetime import datetime

class Account:
    def __init__(self):
        self.balance: int = 0
        self.history: list = []

    def deposit(self, amount: int):
        self.balance += amount
        self.history.append({
            'date': datetime.now(),
            'amount': amount,
            'balance': self.balance
        })

    def withdraw(self, amount: int):
        if self.balance < amount:
            print("No tienes ese dinero compa")
            return
        self.balance -= amount
        self.history.append({
            'date': datetime.now(),
            'amount': -amount, 
            'balance': self.balance
        })

    def printStatement(self):
        print(f"{'DATE':<12} | {'AMOUNT':<10} | {'BALANCE':<10}")
        for transaction in reversed(self.history):
            date_str = transaction['date'].strftime("%d/%m/%Y")
            amount = transaction['amount']
            balance = transaction['balance']
            print(f"{date_str:<12} | {amount:<10} | {balance:<10}")

def main():
    test = Account()
    test.deposit(500)
    test.withdraw(100)
    test.printStatement()

if __name__ == "__main__":
    main()