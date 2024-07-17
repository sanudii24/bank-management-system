#Users Registration SignUp and SignIn
import random
from bank import*
from database import *
from customer import*
def SignUp():
    username=input("Create Username: ")
    temp=db_query(f"SELECT username FROM customers where username='{username}'")
    if temp:
        print("Username Already Exists")
        SignUp()
    else:
        print("Username is Available Please Proceed")
        password=input("Enter your password : ")
        name=input("Enter Your Name : ")
        age=input("Enter Your Age : ")
        city=input("Enter Your City : ")
        while True:
            account_number=int(random.randint(10000000,99999999))
            temp=db_query(f"SELECT account_number FROM customers WHERE account_number='{account_number}';")
            if temp:
                continue
            else:
                print("Your Account Number : ",account_number)
                break
    Customerobj=Customer(username,password,name,age,city,account_number)
    Customerobj.createuser()
    Customerobj=Bank(username,account_number)
    Customerobj.Create_transaction_table()
def SignIn():
    username=input("Enter Username : \n")
    temp=db_query(f"SELECT username FROM  customers WHERE username='{username}';")
    if temp:
        while True:
            password=input(f"Welcome {username.capitalize()} \n Enter Password : \n")
            temp=db_query(f"SELECT password FROM customers WHERE username='{username}';")
            #print(temp[0][0])
            if temp[0][0]==password:
                print("Sign In Successfully ")
                return username
            else:
                print("Wrong Password Try Again : \n")
                continue

    else:
        print("Enter Correct Username : \n")
        SignIn()
