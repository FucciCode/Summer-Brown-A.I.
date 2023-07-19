import time

# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk

class SocialNetwork:
    def __init__(self):
        Nick = Person("Nick", 17)
        Logan = Person("Logan", 16)
        Siena = Person("Siena", 16)
        Henry = Person("Henry", 3)

        self.list_of_people = [Nick, Logan, Siena, Henry] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
        self.current_person = Person("", 0)
        
    ## For more challenge try this
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

    def  create_account(self, user, age):
        #implement function that creates account here
        print("Creating ...")
        time.sleep(1)
        print("")
        self.list_of_people.append(Person(user, age))
        print("Account created! Please login.\n")
        print("-----------------------------------\n")
        time.sleep(1)


    def getUser(self, user): #returns true if the user exists
        for x in range(len(self.list_of_people)):
            if self.list_of_people[x].getName() == user:
                return True
        return False
    
    def getCurrent(self): #returns the current user, also allows me to access Person class functions
        return self.current_person

        
    def setCurrent(self, user): #searches list of people for the given name, and sets them as the current user
        for x in range(len(self.list_of_people)):
            if self.list_of_people[x].getName() == user:
                self.current_person = self.list_of_people[x]
    
    def getPerson(self, user): #returns the given user as an object
        for x in range(len(self.list_of_people)):
            if self.list_of_people[x].getName() == user:
                return self.list_of_people[x]





        
    
    

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friendlist = []
        self.blockList = []
        self.messageList = []

    def add_friend(self, friend):
        #implement adding friend. Hint add to self.friendlist
        self.friendlist.append(friend)
        

    def block_person(self, blockUser):
        self.blockList.append(blockUser)
        if self.searchFriends(blockUser):
            self.friendlist.remove(blockUser)
            print("Person was also removed from your friends list.")
            time.sleep(1)


    def send_message(self, recipitant, network):
        #implement sending message to friend here
        message = input(f"What would you like to say to {recipitant}?")
        recieverObject = network.getPerson(recipitant)
        recieverObject.messageList.append(f"From {self.name}:" + message)


    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def changeName(self, newName):
        self.name = newName

    def changeAge(self, newAge):
        self.age = newAge

    def viewFriends(self):
        if len(self.friendlist) == 0:
            print("You don't seem to have any friends, try adding some!")
            time.sleep(1.5)
        else:
            print (self.friendlist)
            time.sleep(1.5)

    def searchFriends(self, friend):
        for x in range(len(self.friendlist)):
            print(self.friendlist[x])
            if self.friendlist[x] == friend:
                return True
        return False
    
    def viewMessages(self):
        if len(self.messageList) == 0:
            print("You have not received any messages.")
        else:
            print(self.messageList)
            time.sleep(1.5)


    def viewBlocked(self):
        if len(self.blockList) == 0:
            print("You don't have anyone currently blocked.")
        else:
            print(self.blockList)
            time.sleep(1.5)

    def viewProfile(self):
        print("")
        print("Your profile: \n")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
