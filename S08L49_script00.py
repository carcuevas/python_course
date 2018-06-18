#for loops examples

## first we need the range function,
#range(initial_index,final_index-1)

for number in range(1,6):
    print(number)


# or we can use without the range as:

for number_2 in [1,2,3,4,5,6]:
    print(number_2)



## Now we want to count the amount of vowels and consonant from a text for example
vowels = 0
consonants = 0

texto = input("Please enter your text: ")

for letter in texto:
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter == " ":
        pass

    else:
        consonants = consonants + 1

print("In the text\n {} \nThere are  {}  vowels and  {} consonants".format(texto,vowels,consonants))
      
    
