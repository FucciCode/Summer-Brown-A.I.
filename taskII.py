def taskTwo():
    
    userDecis = int(input("Would you like to go from hours to minutes or minutes to hours? (1 or 2)"))

    if userDecis == 1:

        userHours = int(input("how many hours?"))
        userToMinutes = userHours * 60
        print(int(userToMinutes))
    else:

        userMinutes = int(input("how many minutes?"))
        userToHours = userMinutes / 60
        print(int(userToHours))

taskTwo()


