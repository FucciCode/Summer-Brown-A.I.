#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_ui
import time



#Create instance of main social network object
ai_social_network = SocialNetwork()



#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    

    while True: 
        
        if choice == "1":
            print("")
            print("\nYou are now in the create account menu")
            persName = input("Create your username: ")
            persAge = input("Enter your age: ")

            ai_social_network.create_account(persName, persAge)

        elif choice == "2":
            loginName = input("\nLog into your existing account here!\n Enter name: ")
            if ai_social_network.getUser(loginName):
                ai_social_network.setCurrent(loginName)
                print("")
                print("Login successful!\n")
                print("\n")
                time.sleep(1.5)

                     #Handle inner menu here

                while True:
                    inner_menu_choice = social_network_ui.manageAccountMenu()
                    if inner_menu_choice == "1":
                        #edit details
                        change_detail = social_network_ui.editDetailsMenu()
                        print(change_detail)
                        if change_detail == "1":
                            #change username
                            new_name = input("What would5 you like to change your name to?")
                            ai_social_network.getCurrent().changeName(new_name)
                            print("")
                            print("Changing name...")
                            time.sleep(1)
                            print("\nName successfully changed!")
                            time.sleep(1)


                        elif change_detail == "2":
                            #change age
                            new_age = input("Enter your updated age here: ")
                            ai_social_network.getCurrent().changeAge(new_age)
                            print("")
                            print("Changing age...")
                            time.sleep(1)
                            print("\nAge successfully updated!")
                            time.sleep(1)

                        
                        else:
                            print("")
                            print("Sorry, that isn't a valid selection, please try again.")
                            time.sleep(1)
                        #end edit details menu


                    elif inner_menu_choice == "2":
                        ai_social_network.getCurrent().viewProfile()
                        time.sleep(1.5)

                    elif inner_menu_choice == "3":
                        #add friend
                        friend = input("Type in the name of your friend you'd like to add here: ")
                        if ai_social_network.getUser(friend):
                            ai_social_network.getCurrent().add_friend(friend)
                        print("Friend added!")
                        time.sleep(1)

                    elif inner_menu_choice == "4":
                        #view all friends
                        
                        print("")
                        print("Friends: ")
                        ai_social_network.getCurrent().viewFriends()
                        

                    elif inner_menu_choice == "5":
                        #send messages
                        messagePerson = input("Who would you like to send a message to?")
                        if ai_social_network.getCurrent().searchFriends(messagePerson):
                            ai_social_network.current_person.send_message(messagePerson, ai_social_network)
                        else:
                            print("Hmm, it doesn't seem like you have this person added. Sorry!")
                            time.sleep(1.5)
                        print("Message sent!\n")
                        time.sleep(1)


                    elif inner_menu_choice == "6":
                        #view all messages
                        print("")
                        print("Inbox: ")
                        ai_social_network.getCurrent().viewMessages()
                        

                    elif inner_menu_choice == "7":
                        #block people
                        blockUser = input("Type in the name of the person you'd like to block here: ")
                        if ai_social_network.getUser(blockUser):
                            ai_social_network.getCurrent().block_person(blockUser)
                        print("Person blocked.")
                        time.sleep(1)

                    elif inner_menu_choice == "8":
                        #block list
                        print("")
                        print("Blocked: ")
                        ai_social_network.getCurrent().viewBlocked()

                    elif inner_menu_choice == "9":
                        print("Directing back to main menu...")
                        time.sleep(1.5)
                        #go back
                        break
                    else:
                        print("")
                        print("Sorry, that selection is invalid, please try again!")
                        time.sleep(1.5)
                        
            
            else:
                print("")
                print("This account doesn't seem to exist, try creating a new one!\n")
                print("------------------------------------------\n")
                time.sleep(2.5)
                choice = social_network_ui.mainMenu()

                 #Handle inner menu here


        elif choice == "3":
            print("")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            print("Thank you for visiting. Goodbye!")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()