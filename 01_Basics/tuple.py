# tuple is imutable but list is mutable 

tea_types = ("Black", "Green", "Oolong")
print(tea_types)
print(tea_types[0])
print(tea_types[-1])
print(tea_types[1:])
# tea_types[0] = "Lemon"
# print(tea_types)

more_tea = ("Herbal", "Earl Grey")
all_tea = more_tea + tea_types
print(all_tea)

if "Green" in all_tea:
    print("I have green tea")

more_tea = ("Herbal", "Earl Grey", "Herbal")
print(more_tea)
print(more_tea.count("Herbal"))
print(more_tea.count("Herb"))