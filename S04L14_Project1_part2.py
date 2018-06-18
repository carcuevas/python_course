##################
# Health project
##################

## We are going to import the random module

import random 



health = 50

# difficult 1 easy, 2 medium and 3 hard
difficulty = 3 #easy mode by default

## Random number between 25 - 50

potion_health = int(random.randint(25,50) / difficulty)  #we use int casting for not getting floats

health = health + potion_health
print(health)
