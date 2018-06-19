#Pig Latin translator


# Simple joke, which make simple words difficult to understand, for example if we have:
# pig -> igPay
# happy -> appyHay
# glove -> oveGlay
# apple -> appleyay
##
### Basically we take the first consonant from the word and we put it at the end of the word, and we add 'ay' at the end.
# And if the word start with vowel, we just add 'yay'



# So we will ask the user for a sentence and we will convert the whole sentence into "Pig Latin" ;-)
# We ask for the sentence

original = input("Please enter your sentence: ").strip().lower()


# split sentence into words
### For this we are going to use the string method split, will return a list of words

words = original.split()
print("This is your original sentence after the split: ",words)


# loop through the words and convert to pig latin

new_words = []

for word in words: 
# if the first letter is a vowel, just add "yay"
    if word[0] in "aeiou":
        new_word = word + "yay"
        # So now we can add the new word to our list new_words
        new_words.append(new_word)

    else:
    #otherwise, move the first consonant cluster to end and add "ay"
        vowel_pos = 0 # vowel position in the word
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                # we foound a vowel so we dont need to continue looking for eat so we stop this loop
                break
            # now we will have to  get an slice of the words from where the vowel start and store them  
        consonants = word [:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + consonants + "ay"
        # So now we can add the new word to our list new_words
        new_words.append(new_word)
    
         
# stick words back together into sentence

    #for this we will use the " ".join method, which will make an string from the contents of the list, and separated with the character between " "
output = " ".join(new_words)


# output the  final string

print(output)


