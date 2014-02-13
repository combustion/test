class Player:
    name = ""
    powers = {}
    def __init__ (self, n):
        self.name = n

p = Player("harry")

print (p)
p.powers = {1,2,3,4,5}
print (p.powers)
#print (p.powers.contains(1))

def mul2(o, x):
    return x*2

Player.f = mul2
print(p.f(2))
