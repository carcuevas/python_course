#List Comprehension

# for the example, if we want to create a list with the even number between 1 and 100 in one line of code
even_numbers = [x for x in range(1,100) if x%2 ==0 ]
print(even_numbers)

# Another more complicated example...

#we have a list of words:
words = ["Ash", "tRay", "machIne", "cars" ]

#then we create our output
answer = [[w.upper(),w.lower(),len(w)] for w in words ]
print(answer)

