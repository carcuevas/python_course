#While loops examples
number = 1

while number <= 10:
    print(number)
    number = number + 1


# other example

L = []


while len(L) < 3:
    new_name = input("Please add a new name: ").strip().capitalize()
    L.append(new_name)

print("Sorry the List L is full ...")
print(L)
