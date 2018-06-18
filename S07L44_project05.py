# Project for cinema ticket reservation

# We create a dictionary with the name as Item, and it will content the rate and the name of free places.
films = {
    "Finding Dory": [3,5],
    "Bourne": [18,5],
    "Tarzan" : [15,5],
    "Ghostbusters" : [12,5],
    }

## Infinite loop
while True:

    #First we ask the user what film he/she wants to watch, will remove spaces and we use title 
     choice = input('What film do you want to watch?: ').strip().title()

    # After we check if the film is on the list
    if choice in films:
        # ask for age
        age = int(input("How old are you?: ").strip())

        
        #we check the age, it's the first element of the items
        if age >= films[choice][0]:

            #Now we check if there are enough of seats
            if films[choice][1] > 0:
                print("enjoy the film!")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Not enough places sorry..")
        else:
            print("You are too young my friend... !!")
        #pass  # this will skip if it's hit
    else:
        print("We do not have this film")

    
 
