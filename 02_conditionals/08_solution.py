# possward cheacker

password = "Secure3@pass"

if len(password) < 6:
    strength = "Weak"
elif len(password) <= 10:
    strength = "Medium"
else: 
    strength = "Strong" 

print("Password stregth is: ", strength)  