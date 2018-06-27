### Making all coins in the Euro system 0.01,0.05, 0.1, 0.2, 0.5, 1, 2 :)

## All the coins have more than less the same properties, so why to define the same thing many times ... better to ...:

### Create an abstract class from which the other coins will inheritate the properties... ;-) 

class Coin:

    #Constructor method
    def __init__(self, rare = False, clean = True, heads = True, **kwargs):  ## the kwargs will be explained later when creating child Coin classes
        # we set our values
        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        # and get all the arguments passed via kwargs as:

        for key, value in kwargs.items():
            setattr(self,key,value)  #### This will go throught the data and set automatically all the data sent from the child class into the new object

        # so we'll define how it will be when the coin is rare
        if self.is_rare:
            self.value = (self.original_value * 1.25 ) # We will set the value a 25% more for rare coins
        else:
            self.value = self.original_value # otherwise we preserve its original value
            
        # and now we'll define how it will be when the coin is clean
        if self.is_clean:
            self.colour = self.clean_colour # No rusted,no change in the colour
        else:
            self.colour = self.rusty_colour # otherwise we preserve its original value


    #Rust method
    def rust(self):     # This method will rust the coin and change the colour to greenish
        self.colour = self.rusty_colour

    #Clean method
    def clean(self):  # Tihs method will return the coin to its natural colour
        self.colour = self.clean_colour

    #flip method
    def flip(self): # this method will randomize the flip of the coin
        heads_options = [True, False] # the coin can be in heads or tails
        choice = random.choice(heads_options) # Will take a random option of the head_options
        self.heads = choice

    #Destructor method
    def __del__(self):  ## This will be the destructor of the objects

        # to delete an object we invoke "del object_name"
        print("Coin spent ! ")
            

class Euro(Coin):  ## as it can be seen, it's inheritating all the states and methods from Coin Class, but we still have to define some values like self.clean_colour

    # We define our constructor for Euro objects
    def __init__(self):
        # so we create a dictionary called data in which we'll pass all properties needed

        data = {
                    "original_value" : 1.00,
                    "rusty_colour"   : "greenish",
                    "clean_colour"   : "silver",
                    "number_edges"   : 1, # it's rounded
                    "diameter"       : 23.25,  # in mm
                    "thickness"      : 2.33, # in mm
                    "mass"           : 7.5  # in gr



                }

        
        super().__init__(**data) ### This will call the Super class, or parent class constructor, and we'll pass our data unpacked to it (meaning key=value for every element of the data )
        # And this is why we have the **kwarks in the constructor of the parent class (we pack back the argument passed)


        

class One_cent(Coin):  ## One cent coint

    # We define our constructor for Euro objects
    def __init__(self):
        # so we create a dictionary called data in which we'll pass all properties needed

        data = {
                    "original_value" : 0.01,
                    "rusty_colour"   : "brownish",
                    "clean_colour"   : "bronze",
                    "number_edges"   : 1, # it's rounded
                    "diameter"       : 16.25,  # in mm
                    "thickness"      : 1.67, # in mm
                    "mass"           : 2.3  # in gr



                }

        
        super().__init__(**data) ### This will call the Super class, or parent class constructor, and we'll pass our data unpacked to it (meaning key=value for every element of the data )
        # And this is why we have the **kwarks in the constructor of the parent class (we pack back the argument passed)


class Two_cents(Coin):  ## One cent coint

    # We define our constructor for Euro objects
    def __init__(self):
        # so we create a dictionary called data in which we'll pass all properties needed

        data = {
                    "original_value" : 0.02,
                    "rusty_colour"   : "brownish",
                    "clean_colour"   : "bronze",
                    "number_edges"   : 1, # it's rounded
                    "diameter"       : 18.75,  # in mm
                    "thickness"      : 1.67, # in mm
                    "mass"           : 3.06  # in gr



                }

        
        super().__init__(**data)


class Five_cents(Coin):  ## One cent coint

    # We define our constructor for Euro objects
    def __init__(self):
        # so we create a dictionary called data in which we'll pass all properties needed

        data = {
                    "original_value" : 0.05,
                    "rusty_colour"   : "brownish",
                    "clean_colour"   : "bronze",
                    "number_edges"   : 1, # it's rounded
                    "diameter"       : 21.25,  # in mm
                    "thickness"      : 1.67, # in mm
                    "mass"           : 3.92  # in gr



                }

        
        super().__init__(**data)

class Ten_cents(Coin):  ## One cent coint

    # We define our constructor for Euro objects
    def __init__(self):
        # so we create a dictionary called data in which we'll pass all properties needed

        data = {
                    "original_value" : 0.10,
                    "rusty_colour"   : "greenish",
                    "clean_colour"   : "gold",
                    "number_edges"   : 1, # it's rounded
                    "diameter"       : 19.75,  # in mm
                    "thickness"      : 1.93, # in mm
                    "mass"           : 4.10  # in gr



                }

        
        super().__init__(**data)

class Twenty_cents(Coin):  ## One cent coint

    # We define our constructor for Euro objects
    def __init__(self):
        # so we create a dictionary called data in which we'll pass all properties needed

        data = {
                    "original_value" : 0.20,
                    "rusty_colour"   : "greenish",
                    "clean_colour"   : "gold",
                    "number_edges"   : 7, # it's rounded but 7 indents
                    "diameter"       : 22.25,  # in mm
                    "thickness"      : 2.14, # in mm
                    "mass"           : 5.74  # in gr



                }

        
        super().__init__(**data)

class Fifty_cents(Coin):  ## One cent coint

    # We define our constructor for Euro objects
    def __init__(self):
        # so we create a dictionary called data in which we'll pass all properties needed

        data = {
                    "original_value" : 0.50,
                    "rusty_colour"   : "greenish",
                    "clean_colour"   : "gold",
                    "number_edges"   : 1, # it's rounded
                    "diameter"       : 24.25,  # in mm
                    "thickness"      : 2.38, # in mm
                    "mass"           : 7.80  # in gr



                }

        
        super().__init__(**data)

class Two_euros(Coin):  ## One cent coint

    # We define our constructor for Euro objects
    def __init__(self):
        # so we create a dictionary called data in which we'll pass all properties needed

        data = {
                    "original_value" : 2.00,
                    "rusty_colour"   : "greenish",
                    "clean_colour"   : "gold",
                    "number_edges"   : 1, # it's rounded
                    "diameter"       : 25.75,  # in mm
                    "thickness"      : 2.20, # in mm
                    "mass"           : 8.50  # in gr



                }

        
        super().__init__(**data)

##


# we create the object coin1_test
print("")
print("")
print("")
print("")
coin1 = Euro()
coin2 = Euro()
print("Type of coin1 is: ",type(coin1))
print("Type of coin2 is: ",type(coin2))
print("For example for the coin1 we have: coin1.colour = {} and coin1.value = {}".format(coin1.colour,str(coin1.value)))
print("For the coin2 we have: coin2.colour = {} and coin2.value = {}".format(coin2.colour,str(coin2.value)))

# we rust the coin2
coin2.rust() # we call the method
print("So we can rust the coin2 and coin2.colour will be:  ",coin2.colour)

