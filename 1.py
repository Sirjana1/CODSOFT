# #Hello this is Sirjana Chaudhary. Now i started to practice python that is done on 2nd lab of AI



# class Atm:
#     #constructor
#     def __init__(self):
#         self.pin = ''
#         self.balance = 0
#         self.menu()

 
#     def menu(self):
#         user_input = int(input("""
#             Welcome to Ncit Bank
#                 1. Press 1 to create pin.
#                 2. Press 2 to change pin.
#                 3. Press 3 to check balance.
#                 4. Press 4 to withdraw.
#                 5. Press 5 to exit or any key.
#          """))
#         if user_input == 1:
#             self.createPin()

#         elif user_input == 2:
#             self.changePin()

#         elif user_input == 3:
#             self.checkBalance()
#         elif user_input == 4:
#             self.withdraw()
#         else:
#             print('Have a goood day')
#             exit()

#     def createPin(self):
#         user_pin = print('Enter your pin: ')
#         if len(user_pin)<4:
#             print('The enter pin is less than 4, Please enter total 4 digits')
#             self.createPin()
#         else:
#             self.pin == user_pin
#             user_balance = int(input('Enter balance: '))
#             self.balance == user_balance
#             print('Pin created sucessfully.')
#             self.menu()
    

#     def changePin(self)
#         if self.pin == input('Input current pin:'):
#            self.pin == input('Input new pin:')
#            print('pin changed successfully.')
#         else:
#             print('Incorrect pin')
#             self.menu()
    

#     def checkBalance(self)
#         user_pin = print('Enter your pin:')
#         if self.pin == user_pin:
#             print('Your current balance is:', self.balance)
#             print('Incorrect balance.')  
#             self.menu()   

#     def withdraw(self):
#         user_pin = input('Enter your pin:') 
#         if self.pin == user_pin:
#             amount = int(input('Enter the amount to withdraw'))
#             if amount>= self.balance:
#                 print('Insufficient balance.')
#             else:
#                 self.balance -= amount
#                 print('Withdraw successfully. Your current balance is:', self.balance)
class Atm:
    # Constructor
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = int(input("""
            Welcome to Ncit Bank
                1. Press 1 to create pin.
                2. Press 2 to change pin.
                3. Press 3 to check balance.
                4. Press 4 to withdraw.
                5. Press 5 to exit or any key.
         """))
        if user_input == 1:
            self.createPin()
        elif user_input == 2:
            self.changePin()
        elif user_input == 3:
            self.checkBalance()
        elif user_input == 4:
            self.withdraw()
        else:
            print('Have a good day')
            exit()

    def createPin(self):
        user_pin = input('Enter your pin: ')
        if len(user_pin) < 4:
            print('The entered pin is less than 4, Please enter a total of 4 digits')
            self.createPin()
        else:
            self.pin = user_pin
            user_balance = int(input('Enter balance: '))
            self.balance = user_balance
            print('Pin created successfully.')
            self.menu()

    def changePin(self):
        if self.pin == input('Input current pin: '):
            self.pin = input('Input new pin:')
            print('Pin changed successfully.')
        else:
            print('Incorrect pin')
            self.menu()

    def checkBalance(self):
        user_pin = input('Enter your pin:')
        if self.pin == user_pin:
            print('Your current balance is:', self.balance)
        else:
            print('Incorrect pin.')
        self.menu()

    def withdraw(self):
        user_pin = input('Enter your pin:')
        if self.pin == user_pin:
            amount = int(input('Enter the amount to withdraw: '))
            if amount > self.balance:
                print('Insufficient balance.')
            else:
                self.balance -= amount
                print('Withdrawal successful. Your current balance is:', self.balance)
        else:
            print('Incorrect Pin')
        self.menu()


# Example usage
if __name__ == "__main__":
    atm = Atm()

        
        
