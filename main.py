def show_balance(balance):
    print("*" * 30)
    print(f"your balance is {balance:.2f}$")
    print("*" * 30)
def deposit():
    print("*" * 30)
    amount = float(input("enter the amount to deposit: "))
    print("*" * 30)
    if amount < 0:
        print("*" * 30)
        print("please enter a valid amount")
        print("*" * 30)
        return 0
    else:
        return amount
def withdraw(balance):
    print("*" * 30)
    amount = float(input("enter the amount to withdraw: "))
    print("*" * 30)
    if amount > balance:
        print("*" * 30)
        print("insufficient funds")
        print("*" * 30)
        return 0
    elif amount < 0:
        print("*" * 30)
        print("amount must be positive")
        print("*" * 30)
        return 0
    else:
        return amount

def main():

   balance = 0
   is_running = True
   while is_running:
        print("*"*30)
        print("           BANKING PROGRAM         ")
        print("1.show balance")
        print("2.deposit")
        print("3.withdraw")
        print("4.exit")
        print("*"*30)

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
           show_balance(balance)
        elif choice == "2":
           balance += deposit()
        elif choice == "3":
           balance -= withdraw(balance)
        elif choice == "4":
           is_running = False
        else:
           print("*" * 30)
           print("Please enter a valid choice")
           print("*" * 30)
   print("*" * 30)
   print("thanks you, have a nice day")
   print("*" * 30)
if __name__ == "__main__":
    main()
