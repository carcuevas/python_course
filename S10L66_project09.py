# Making our own Coin using classes

import random  # We import the random for flipping the coin

## First we create a class for creating 1Euro coin
class Euro_test:
    ## Our states (variables) which defines the Euro coin
    value = 1.00
    colour = "gold"
    num_edges = 1 ## it's a circular coin
    diameter = 23.25 ## in mm
    thickness = 2.33 ## in mm
    heads = True
     


# we create the object coin1_test

coin1_test = Euro_test()
print("Type of coin1 is: ",type(coin1_test))
print('''Let's print the colour (state) of the coin1: ''',coin1_test.colour)

### So now we can define our Euro class properly with a constructor:

class Euro:
    def __init__(self, rare = False): #this is the noatation for the constructor, rare is some extra parameter which will tell us if the coin is rare and if it is we will increase a bit the value
        ## Our states (variables) which defines the Euro coin


        ## The self is needed because that will be substituted with our object name when calling the constructor
            
        self.rare = rare    
        self.colour = "gold"
        self.num_edges = 1 ## it's a circular coin
        self.diameter = 23.25 ## in mm
        self.thickness = 2.33 ## in mm
        self.heads = True
        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00


    def rust(self):     # This method will rust the coin and change the colour to greenish
        self.colour = "greenish"

    def clean(self):  # Tihs method will return the coin to its natural colour
        self.colour = "gold"

    def flip(self): # this method will randomize the flip of the coin
        heads_options = [True, False] # the coin can be in heads or tails
        choice = random.choice(heads_options) # Will take a random option of the head_options
        self.heads = choice

    def __del__(self):  ## This will be the destructor of the objects

        # to delete an object we invoke "del object_name"
        print("Coin spent ! ")



##


# we create the object coin1_test
print("")
print("")
print("")
print("")
coin1 = Euro()
coin2 = Euro(rare = True)
print("Type of coin1 is: ",type(coin1))
print("Type of coin2 is: ",type(coin2))
print("For example for the coin1 we have: coin1.colour = {} and coin1.value = {}".format(coin1.colour,str(coin1.value)))
print("For the coin2 we have: coin2.colour = {} and coin2.value = {}".format(coin2.colour,str(coin2.value)))

# we rust the coin2
coin2.rust() # we call the method
print("So we can rust the coin2 and coin2.colour will be:  ",coin2.colour)

