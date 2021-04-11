import random
import time
database = {
    'Ch20953': ['Chinasa', 'Anele', '2222', 'atmmockpractice@zuriteam.co', '3410120953', 80000 ]
}
feedback = ["Please take your cash", "Thank you for contacting us."]



def register():
    print("========= Please fill in the following information to create an account =========")
    email = input("Email address: ")
    firstName = input("First Name: ")
    lastName = input("Last Name: ")
    password = (input("Password: "))
    accountNum = str(random.randrange(1111111111,9999999999))
    userId = firstName[:2].capitalize() + (accountNum[-5:])
      

    if len(password) != 4:
        print("Password character must not be more than 4 digits, try again!")
    else:
        confirmPassword = input("Confirm password: ")

        if confirmPassword == password:
            print("Generating account, please wait")
            time.sleep(3)
            print("Account creation successful!")
            print("       ♦♦♦♦♦♦♦♦♦♦♦♦»»»»»»»»»»»»»♦♦♦♦♦♦♦♦♦♦♦♦      ")
            print("Your account number is {} and username {}.".format(accountNum,userId))
            print("Please keep your details safe")
            print("       ♦♦♦♦♦♦♦♦♦♦♦♦»»»»»»»»»»»»»♦♦♦♦♦♦♦♦♦♦♦♦      ")
            time.sleep(3)

            database[userId] = [ firstName, lastName, password, email, accountNum, 0 ]

            login()
        else:
            print("Password does not match!")
            register()

def login():

    print("  >>>> Input your details to login <<<<  ")

    userIdFromUser = input("UserID: ")
    passwordFromUser = input("Password: ")
    for userId, userDetails in database.items():
        if(userId == userIdFromUser):
            if(userDetails[2] == passwordFromUser):
                bankOperation(userDetails)

            else:
                print('Invalid account or password')
                login()





def init():
    print("     ¤¤¤¤¤¤¤¤¤¤¤¤¤  WELCOME TO PRATZ BANK™   ¤¤¤¤¤¤¤¤¤¤¤¤¤    ")
    print("Do you have an account with us?")
    print("1. Yes")
    print("2. No")

    operation = int(input("Please select an option: "))
    if (operation == 1):
        login()

    elif (operation == 2):
        register()
    else:
        print("You have selected an invalid option")
        init()
        

def currentBalance(userDetails):
    return userDetails[5]


def anotherTransaction():
    secondTransaction = int(input("Would you like to perform another transaction? \n 1. Yes or 2. No \n"))

    if(secondTransaction == 1):
        login()

    elif(secondTransaction == 2):
        print("   ¤¤¤¤¤¤¤¤¤¤¤¤¤  THANK YOU FOR BANKING WITH PRATZ BANK™   ¤¤¤¤¤¤¤¤¤¤¤¤¤   ")
        exit()

    else:
        print("Goodbye!")
    
    
def withdrawal(userDetails):
    currentBalance(userDetails)
    withdrawal = int(input("How much would you like to withdraw? \n"))

    if(withdrawal <= currentBalance(userDetails)):
        print(feedback[0])
        print("Current balance: ", currentBalance(userDetails) - withdrawal)
        anotherTransaction()

    else:
        print("Insufficient funds! Try again")
        anotherTransaction()


def deposit(userDetails):
    currentBalance(userDetails)
    deposit = int(input("How much would you like to deposit? \n"))
    if deposit >= 1000:
        print("Deposit Successful!, Current balance:", deposit + currentBalance(userDetails))
        anotherTransaction()
       
    else:
        print("Input a valid amount")

        

def complaint():
    complaint = input("What issue would you like to report? \n")
    print(feedback[1])

def logout():
    init()



def bankOperation(userDetails):
    import datetime
    currentTime = datetime.datetime.now()

    print("♦♦♦♦♦♦♦♦♦♦♦♦    You are Loggedin    ♦♦♦♦♦♦♦♦♦♦♦♦")

    print("Welcome {}, what would you like to do today?".format(userDetails[0]))
    print(currentTime)
    print("These are the available options:")
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')
    print('4. Logout')
    print('5. Exit')

    Option = int(input('Pick an option to initiatiate an action: '))

    if(Option == 1):
        withdrawal(userDetails)

    elif(Option == 2):
        deposit(userDetails)

    elif(Option == 3):
        complaint()

    elif(Option == 4):
        logout()

    elif(Option == 5):
        print("   ¤¤¤¤¤¤¤¤¤¤¤¤¤  THANK YOU FOR BANKING WITH PRATZ BANK™   ¤¤¤¤¤¤¤¤¤¤¤¤¤   ")
        exit()

    else:
        print("Invalid option, please try again!")
        bankOperation(userDetails)


"""
Main Bank Operation
"""          

init()