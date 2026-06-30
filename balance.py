from bank import Bank


class Balance(Bank):

    # ---------- Polymorphism ----------
    def operation(self):
        print("\n========== Balance Enquiry ==========")

    # ---------- Show Balance ----------
    def show_balance(self, user):

        self.operation()

        try:
            balance = user.get_balance()

            if balance is not None:
                print(f"Current Balance : ₹{balance}")
            else:
                print("Unable to fetch balance.")

        except AttributeError:
            print("Invalid user object.")

        except Exception as e:
            print("Something went wrong:", e)

        finally:
            print("====================================")