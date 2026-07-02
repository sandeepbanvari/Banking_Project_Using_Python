import re

from bank import Bank
from customers import Customer
from filehandler import FileHandler


class Signup(Bank):

    def __init__(self):

        self.file = FileHandler()

    # ---------- Polymorphism ----------

    def operation(self):

        print("\n========== User Registration ==========")

    # ---------- Signup ----------

    def signup(self):

        self.operation()

        customers = self.file.load_users()

        username = input("Enter Username : ").strip().lower()
        
        if not re.fullmatch(r"^[A-Za-z0-9_]{3,15}$", username):

            print("\n❌ Invalid Username.")
            print("Username must be alphanumeric and between 3 and 15 characters long.")
            return
            

        found = False

        for user in customers:

            if user.get_username() == username:

                found = True
                break

        if found:

            print("\n❌ Username already exists.")
            print("Please choose a different username.")
            return

        name = input("Enter Full Name : ")
        
        if not re.fullmatch(r"^[A-Za-z ]{3,30}$", name):
            print("\n❌ Invalid Name.")
            print('Name should contain only alphabets and spaces.')
            return

        try:

            age = int(input("Enter Age : "))

        except Exception as msg:

            print("\n❌ Invalid Age.", msg)
            return

        email = input("Enter your email : ")
        
        if not re.fullmatch(r'^[A-Za-z0-9._%-]{2,}+@[\w]{2,}\.[\w]{2,}$', email):
            print('\n❌ Invalid email.')
            return

        password = input("Enter Password : ")
        
        if not re.fullmatch(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$', password):
            print('\n❌ Invalid Password.')
            return

        try:

            balance = int(input("Enter Opening Balance (₹): "))

        except Exception as msg:

            print("\n❌ Invalid Opening Balance.", msg)
            return

        user = Customer(

            name,
            age,
            username,
            email,
            password,
            balance

        )

        customers.append(user)

        self.file.save_users(customers)

        print("\n======================================")
        print("🎉 Account Created Successfully!")
        print(f"👤 Welcome, {name}")
        print(f"🆔 Username : {username}")
        print(f"💰 Opening Balance : ₹{balance}")
        print("🏦 Thank you for choosing Python Bank.")
        print("======================================")