#Functions

# We define a function which add two numbers

def add_numbers(x,y):
    return x + y


# we define a function to reverse some word

# for reversing a word we use the slice trick [::-1]
def rev(text):
    return text[::-1]







answer = add_numbers(5,10)
print("For add_number function the result is: ",answer)

word = input("Enter the word you want to be reversed: ").strip().lower()

print("Your inverted word is: ",rev(word))

