from bank import Bank
from filehandler import FileHandler
from deposit import Deposit
from withdraw import Withdraw
from balance import Balance


class Login(Bank):

    def __init__(self):

        self.file = FileHandler()

    # ---------- Polymorphism ----------

    def operation(self):

        print("\n========== Login ==========")

    # ---------- Login ----------

    def login(self):

        self.operation()

        customers = self.file.load_users()

        username = input("Enter Username : ").strip().lower()
        password = input("Enter Password : ")

        found = False

        for user in customers:

            if username == user.get_username() and password == user.get_password():

                found = True

                print("\n======================================")
                print(f"✅ Login Successful!")
                print(f"👋 Welcome, {user.get_name()}")
                print("======================================")

                while True:

                    print("""
======================================
            BANK MENU
======================================
1. 💰 Deposit
2. 💸 Withdraw
3. 🏦 Check Balance
4. 🚪 Logout
======================================
""")

                    try:
                        option = int(input("👉 Enter Your Choice : "))

                    except Exception as msg:
                        print(f"\n❌ Invalid Input: {msg}")
                        continue

                    match option:

                        case 1:

                            deposit = Deposit()

                            success = deposit.deposit(user)

                            if success:

                                self.file.save_users(customers)

                                self.file.save_transaction(

                                    user.get_username(),
                                    "Deposit",
                                    deposit.amount,
                                    user.get_balance()

                                )

                        case 2:

                            withdraw = Withdraw()

                            success = withdraw.withdraw(user)

                            if success:

                                self.file.save_users(customers)

                                self.file.save_transaction(

                                    user.get_username(),
                                    "Withdraw",
                                    withdraw.amount,
                                    user.get_balance()

                                )

                        case 3:

                            balance = Balance()

                            balance.show_balance(user)

                        case 4:

                            print("\n🚪 Logout Successful.")
                            print("🙏 Thank you for banking with us!")
                            break

                        case _:

                            print("\n❌ Invalid Choice.")
                            print("Please select an option between 1 and 4.")

                break

        if found == False:

            print("\n❌ Invalid Username or Password.")
            print("Please check your credentials and try again.")