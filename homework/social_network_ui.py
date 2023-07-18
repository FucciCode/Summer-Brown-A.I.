# You can implement user interface functions here.

def mainMenu():
    print("")
    print("1. Create a new account")
    print("2. Login")
    print("3. Quit")
    print("********************************************************")
    return input("Please choose a number: ")

def manageAccountMenu():
    print("")
    print("1. Edit my details")
    print("2. View my profile")
    print("3. Add a friend")
    print("4. View all my friends")
    print("5. Send message")
    print("6. View messages")
    print("7. Block someone")
    print("8. Block list")
    print("9. <- Log out")
    return input("Please choose a number: ")

def editDetailsMenu():
    print("")
    print("1. Change username")
    print("2. Correct age")
    return input("Please chose a number: ")
