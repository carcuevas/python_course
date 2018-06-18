 
### This the proyect called hello_you


# Ask user for name

name = input('''What's your name?: ''')

# Ask user for age

age = int(input('''How old are you?: '''))

# Ask user for city

city = input('''In which city are you living?: ''')

# Ask user what they enjoy 

love = input('''What do you love to do?: ''')

# Create output text

string = "Your name is {} and you are {} years old. You live in {} and you love {}"
output_string = string.format(name,age,city,love)
 
# Print output to screen

print(output_string)
