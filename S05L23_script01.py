

# for testing methods

a = "hello"
b = "happy biRthday"

print("original a:" "{}".format(a))
print("original b:" "{}".format(b))

# Example of methods

# Count method

print(a.count("e"))
print(b.count("day"))

# lower method
print(b.lower())

# upper method
print(b.upper())
  
# capitalize method (just uppercase the first letter)
print(a.capitalize())

# title method (capitalize every word in the string)
print(b.title())

# islower and isupper methods (will check if the whole text is in lowercase/uppercase)
print(b.islower())
print(b.isupper())

# istitle method similar like isupper but just for the words first letter
print(a.istitle())

# isalpha checks if the string contains only letters (spaces are not inlcluded !!)
print(a.isalpha())

# isdigit check if the string only contains numbers
print(a.isdigit())

# isalnum check if the string contains combinations of number of leters
print("12cacaeWEe".isalnum())


 
