chai_types = {"masala": "spicy", "ginger": "zesty", "green": "mild"}
print(chai_types)
print(chai_types["masala"])
print(chai_types.get("ginger"))

for chai in chai_types:
    print(chai)


for chai in chai_types :
    print(chai, chai_types[chai])

for key , value in chai_types.items():
    print(key, value)

if "masala" in chai_types:
    print("I have a masala chai")

print(len(chai_types))

chai_types["Earl Grey"] = "Citrus"
print(chai_types)
print(chai_types.pop("ginger"))
print(chai_types.popitem())
print(chai_types)
del chai_types["green"]
print(chai_types)
chai_types_copy = chai_types.copy()
print(chai_types)

tea_shop = {
    "chai":{"Masala" : "Spicy" , "Ginger": "Zesty"},
    "Tea" : {"Green": "Mild" , "Black": "Strong"}}
print(tea_shop)
print(tea_shop["chai"])
print(tea_shop["chai"]["Ginger"])

squared_num = {x:x**2 for x in range(6)}
print(squared_num)
squared_num.clear()
print(squared_num)

keys = ["Masala", "Ginger", "Lemon"]
default_value = "Delicious"
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)
new_dict = dict.fromkeys(keys, keys)
print(new_dict)
