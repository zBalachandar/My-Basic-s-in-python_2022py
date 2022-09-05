user_1 = {
    "Name" : "Selvi.B",
    "Age"  : 40,
    "State" : "Upper_State",
    "SuperSpecies" :True
}
print(type(user_1))
print(user_1["Name"])
print(user_1.values())

print("---------------------------------------")


for t in user_1.items():
    print(t)    