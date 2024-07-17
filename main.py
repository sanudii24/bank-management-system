from register import *
from bank import*
status=False
print(" *** WElCOME TO BANK ***")
while True:
    try:
        register =int(input(" 1. SignUp \n 2. SignIn \n "))
        if register==1 or register==2:
            if register==1:
                SignUp()
            if register==2:
                user=SignIn()
                status=True
                break
                
        else:
            print("Please Enter Valid Input From Options")

    except ValueError:
        print("Invalid Input Try Again With Numbers")


account_number = db_query(f"SELECT account_number FROM customers WHERE username = '{user}';")

def menu(status):
    while status:
        print(f"Welcome {user.capitalize()} Choose Your Banking Service\n")
        
        try:
            facility = int(input("1. Balance Enquiry\n"
                                "2. Cash Deposit\n"
                                "3. Cash Withdraw\n"
                                "4. Fund Transfer\n"
                                "5. Exit \n"
                                ))
            match facility:
                case 1:
                    bobj = Bank(user, account_number[0][0])
                    bobj.balanceequiry()
                
                case 2:
                    try:
                        amount = int(input("Enter Amount to Deposit : "))
                        bobj = Bank(user, account_number[0][0])
                        bobj.deposit(amount)
                        mydb.commit()
                        menu(status)

                    except ValueError:
                        print("Enter Valid Input ie. Number ")
                            

                case 3:
                    try:
                        amount = int(input("Enter Amount to Withdraw : "))
                        bobj = Bank(user, account_number[0][0])
                        bobj.withdraw(amount)
                        mydb.commit()
                        menu(status)

                    except ValueError:
                        print("Enter Valid Input ie. Number")
                            
                case 4:
                    try:
                        receive = int(input("Enter Receiver Account Number : "))
                        amount = int(input("Enter Money to Transfer : "))
                        bobj = Bank(user, account_number[0][0])
                        bobj.fundtransfer(receive, amount)
                        mydb.commit()
                        menu(status)
                    except ValueError:
                            print("Enter Valid Input ie. Number")
                            
                case 5:
                    exit()
                case default:
                    print("Please Enter Valid Input From Options")
                    menu(status)

        except ValueError:
            print("Invalid Input Try Again with Numbers")
            continue
menu(status)