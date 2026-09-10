tea_varieties = ["Black", "green", "Oolong","White"]

print(tea_varieties[-1])

tea_varieties[1:2] = "Lemon"
print(tea_varieties)

tea_varieties = ["Black", "green", "Oolong","White"]
print(tea_varieties[1:2])

tea_varieties[1:2] = ["Lemon"]
print(tea_varieties)
print(tea_varieties[1:3] )

tea_varieties[1:3] = ["green", "Masala"]
print(tea_varieties)
print(tea_varieties[1:1])

tea_varieties[1:1] = ["test", "test"]
print(tea_varieties)
print(tea_varieties[1:2])
tea_varieties[1:3] =[]
print(tea_varieties)

tea_varieties = ["Black", "green", "Oolong","White"]
print(tea_varieties)
for tea in tea_varieties:
    print(tea)

for tea in tea_varieties:
    print(tea, end="-")

tea_varieties = ["Black", "green", "Oolong","White"]

if "Oolong" in tea_varieties:
    print("I have Oolong tea")

tea_varieties = ["Black", "green", "Oolong","White"]
print(tea_varieties.pop())

print(tea_varieties.remove("green"))

print(tea_varieties)

tea_varieties.insert(1, "green")
print(tea_varieties)

tea_varieties_copy = tea_varieties.copy()
tea_varieties_copy.append("lemon")
print(tea_varieties)
print(tea_varieties_copy)

squared_nums = [x**2 for x in range (10)]
print(squared_nums)

