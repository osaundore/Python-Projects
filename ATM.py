balance = 20000
pin = 1234

print("Welocome to the Atm")
entered_pin = int(input("Enter your pin: "))

if entered_pin == pin:
    print("Login successful")
    
    choice = 0
    while choice != 4:
        print("\n1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Your balance is:", balance)

        elif choice == 2:
            withdraw = int(input("Enter amount to withdraw:"))
            if withdraw <= balance:
                balance = balance - withdraw
                print("Please collect your cash")
            else:
                print("Insufficient Balance")

        elif choice == 3 :
            deposit = int(input("Enter amount to deposit:"))
            balance = balance + deposit
            print("Amount Deposited")

        elif choice == 4:
            print("Thank you for using ATM")

        else:
            print("Invalid choice")

    