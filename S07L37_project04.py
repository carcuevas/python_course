## project4 Travis security system

## List of known_users

known_users = [ "Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry" ]


#Infinitive loop
while True:
    print("Hi! My name is Travis")
    # we strip it and capitalize it the name just to have the same like we have it 
    name = input("What's your name? ").strip().capitalize()
    # now we want to check if the name exist in known_users
    # for that we wiil use the 'in' which will give a boolean True/False
    # if it finds or not the element specified in the list
    if name in known_users:
        print("\nHello " "{}" "!!".format(name))
        remove = input("Would you like to be removed from the system? [y/n] ").strip().lower()
        if remove == "y":
            ##@@ .remove(element) is a method for deleting the element from a list
            known_users.remove(name)
        elif remove == "n":
            print("No problem I will keep you in the db")
    
            
    else:
        print("\nHello " "{}" ", your name is not recognised".format(name))
        add_me = input("Would you like to be added to the system? [y/n] ").strip().lower()
        if add_me == "y":
            ##@@ append(element) is a method which is appending an item to the end of the specied list
            known_users.append(name)
        elif add_me == "n":
            print("No problem I will not add you in the db\n\n")

    print("List of users is: " "{}" "\n\n\n".format(known_users))
