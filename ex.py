from signup import Signup
from login import Login

signup = Signup()
login = Login()

print("\n" + "=" * 45)
print("        🏦 WELCOME TO PYTHON BANK 🏦")
print("=" * 45)

while True:

    print("""
=============================================
1. 📝 Signup
2. 🔐 Login
3. ❌ Exit
=============================================
""")

    try:
        choice = int(input("👉 Enter Your Choice: "))

    except Exception as msg:
        print(f"\n❌ Invalid Input: {msg}")
        print("Please enter a valid number.\n")
        continue

    match choice:

        case 1:
            print("\n📝 Redirecting to Signup...\n")
            signup.signup()

        case 2:
            print("\n🔐 Redirecting to Login...\n")
            login.login()

        case 3:
            print("\n🙏 Thank You for Using Python Bank.")
            print("💙 Have a Great Day!")
            print("=" * 45)
            break

        case _:
            print("\n❌ Invalid Choice!")
            print("Please select an option between 1 and 3.\n")