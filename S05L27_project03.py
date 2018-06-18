## Project for email slicer
# So we are going to ask the user for email and we are going to slice the username and the domainfrom the email


#get the user email address, stripping the blank spaces

email = input("what is your email address? : ").strip()

# slice the username

user = email[:email.index("@")]

# slice the domain
domain = email[email.index("@") + 1:]

# format message

output = "Your user name {} and your domain name is {}".format(user,domain)



# display the ouput message
print(output)
