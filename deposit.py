from bank import Bank


class Deposit(Bank):

    def __init__(self):
        self.amount = 0

    # ---------- Polymorphism ----------

    def operation(self):
        print("\n========== Deposit Operation ==========")

    # ---------- Deposit ----------

    def deposit(self, user):

        self.operation()

        try:
            self.amount = int(input("Enter Deposit Amount (₹): "))

        except Exception as msg:
            print("❌ Invalid input.", msg)
            return False

        if self.amount <= 0:
            print("❌ Deposit amount must be greater than ₹0.")
            return False

        balance = user.get_balance()

        balance = balance + self.amount

        user.set_balance(balance)

        print("\n✅ Deposit Successful!")
        print(f"💰 Deposited Amount : ₹{self.amount}")
        print(f"🏦 Available Balance: ₹{user.get_balance()}")
        print("======================================")

        return True