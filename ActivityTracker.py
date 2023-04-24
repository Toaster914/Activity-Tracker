'''
Activity Tracker
Toaster914 & Pawnol
4/21/23
'''

import os

def main_menu():
    '''
    Main menu for the application.
    '''
    while True:
        print("1 - Create account")
        print("2 - Delete account")
        print("3 - Login")
        print("4 - Exit")
        option = int(input("Please enter your selection (1-4) >> "))

        if option == 1:
            create_account()
        elif option == 2:
            delete_account()
        elif option == 3:
            login()
        elif option == 4:
            break
        else:
            print("Invalid selection!")
        print()

def create_account():
    '''
    Creates a new account if one does not exist. If an account
    already exists, no account is created.
    '''
    name = input("Enter the name you want associated with the account >> ").lower().strip()
    if os.path.exists(name + ".txt"):
        print("That account already exists!")
    else:
        file = open(name + ".txt", "x")
        file.close()
        print("The account was created succesfully!")
    print()

def delete_account():
    '''
    Deletes an account if it exists.
    '''
    name = input("Enter the name of the user you want deleted >> ").lower().strip()
    if os.path.exists(name + ".txt"):
        os.remove(name + ".txt")
        print("The account was deleted succesfully!")
    else:
        print("No account exists under that name!")
    print()

def login():
    '''
    logs into the users account if it exists. calls the account
    menu if it exists.
    '''
    name = input("Enter the name of the user you want to login to >> ").lower().strip()
    if os.path.exists(name + ".txt"):
        account_menu(name + ".txt")
    else:
        print("No account exists under that name!")
    print()

def account_menu(file_name):
    '''
    Account menu. Allows user to log, delete, and veiw activities.
    '''
    print()
    while True:
        print("1 - Log activities")
        print("2 - Delete activities")
        print("3 - Veiw activities")
        print("4 - Exit")
        option = int(input("Please enter your selection (1-4) >> "))
        print()

        if option == 1:
            log_activities(file_name)
        elif option == 2:
            delete_activities(file_name)
        elif option == 3:
            veiw_activities(file_name)
        elif option == 4:
            break
        else:
            print("Invalid selection!")

def log_activities(file_name):
    '''
    Logs multiple activities to the user's account. Writes the info to the file.
    '''
    repeat = "y"
    while repeat == "y":
        activity_name = input("Enter the name of the activity >> ")
        hours = input("Enter the number of hours you did the activity >> ")
        calories = input("Enter the number of calories the activity burns per hour >> ")
        file = open(file_name, "a")
        file.write(activity_name + "," + hours + "," + calories + "\n")
        file.close()
        repeat = input("Would you like to log another activity? (y/n) >> ")
        print()

def delete_activities(file_name):
    '''
    Deletes multiple activities from the users account
    '''

    file = open(file_name, "r")
    enteries = file.readlines()
    file.close()

    repeat = "y"
    while repeat == "y":
        for i in range(0, len(entries)):
            feilds = entires[i].split(",")
            print(i + 1, "-", feilds[0], "for", feilds[1], "hours")
        index = int(input("Which activity would you like to delete (enter number) >> ")) - 1
        if index < len(entries):
            entries.pop(index)
            print("Activity succesfully deleted!")
        else:
            print("Invalid input. No activity at that number.")
        repeat = input("Do you want to delete another activity? (y/n) >> ")
        print()

    file = open(file_name, "w")
    file.writelines(entires)
    file.close()

def veiw_activities(file_name):
    '''
    Prints all the activities to the console
    '''
    file = open(file_name, "r")
    enteries = file.readlines()
    file.close()

    for i in range(0, len(entries)):
        feilds = entires[i].split(",")
        print(i + 1, "-", feilds[0], "for", feilds[1], "hours")
    print()

main_menu()
