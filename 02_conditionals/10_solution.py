# Recommend a type of of pet food based on the pet's species and age . 
# ( eg , Dog:< 2 years- puppy food, Cat: 5 years - Senior cat food)

# species = input("Enter pet species: ").lower()
# age = int(input("Enter pet age: "))

species = "cat"
age = 3

if species == "dog" and age < 2:
    print("Puppy food")

elif species == "dog" and age >= 2:
    print("Adult dog food")

elif species == "cat" and age < 1:
    print("Kitten food")

elif species == "cat" and age < 7:
    print("Adult cat food")

elif species == "cat" and age >= 7:
    print("Senior cat food")

else:
    print("Pet species not supported")