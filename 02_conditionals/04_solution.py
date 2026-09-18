# Determine if a fruit id ripe , overripe , or unripe based on its color. 
# (eg., Banana: Green - unripe, Yellow - Ripe, Brown - Overripe)

fruit = "Banana" 
color = "Yellow"

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow" :
        print("Ripe")  
    elif color == "Brown":
        print("OverRipe")

else :
    print("not found ")       