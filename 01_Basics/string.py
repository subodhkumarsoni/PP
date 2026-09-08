chai = "lemon, ginger, mint, masala"
print(chai.split())
print(chai.split(", "))
chai = "Masala Chai"
print(chai.find("Chai"))

chai = "Masala Chai Chai Chai"
print(chai.count("Chai"))

chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai"
print(order.format(quantity, chai_type))

# from string to list 

chai_variety = ["Lemon", "Masala", "Ginger" ]
print("".join(chai_variety))
print(" ".join(chai_variety))
print("-".join(chai_variety))
print(", ".join(chai_variety))


# isme length ke sath sath letters ko find kar sakte h aur wo sequence me aayga top to bottom
chai ="Masala chai"
print(len(chai))
for letter in chai:
    print(letter)

chai = "he said, \"masala chai is awesome\" "
print(chai)

chai = r"Masala\nchai"
print(chai)
chai = r"C:\Users\goluk\OneDrive\Desktop\PP\01_Basics"
print(chai)

chai = "  masala chai  "
print(chai[0:7:2])
print(chai.strip("  "))

chai = "i like this program"
chai_split = chai.split()
print(chai_split)

#  dsa problem o string 

s = "i.like.this.program.very.much"
words = s.split(".")
words.reverse()
result = ".".join(words)
print(result)

s = "..geeks.for.geeks."
words = s.split(".")
new_word = []
for word in words:
    if word != "":
        new_word.append(word)
        
new_word.reverse()
result = ".".join(new_word)
print(result)  

s = "vivek"
print(s[1:2:3])