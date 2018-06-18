#Baby Converstion Simulator

from random import choice # We will import the function choice from random lib
# We can do also "import random" but for using it we would need to use random.choice()

# First we make a list of questions to ask

questions = [
                "Why the sky is blue?: ",
                "Why the dogs bark?: ",
                "Why do you like beer?: "
            ]

question = choice(questions)
# we make some question which is going to be random using function
answer = input(question).lower().strip()

while answer != "just because":
    
    # we make why until we get what we want
    answer = input("Why ?: ").lower().strip()

print("OK I see ...")
