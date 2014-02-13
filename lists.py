l = [1,2,3]

print (l)

empty = []
empty.append (5)
print ("this should print [5]")
print (empty) 
empty.append (3434)
print ("this should print [5,3434]")
print (empty) 
empty.append ("asdfdfas")
print ("this shoudl print [5,3434,\"asdfdfas\"]")

# lets create a dictionary for our inventory
inventory = { "iron" : 1, "sword" : 0, "diamond" : 6 }
print (inventory)

print (inventory["sword"])

# does the inventory have an axe?
print (inventory.keys())

if ("sword" in inventory.keys()):
    print ("there is a sword")

#inventory(4["axe",3)

print (inventory("axe"))
