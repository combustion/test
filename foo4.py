#list_1 = ["chicken", "fence", "pig"]
#print(list_1)

#for l in list_1:
   # print (l)
    #i = input()
    #print (l)
    
#list_2 = [list_1,list_1]
#print (list_2)

#list_3 = [list_2,list_2,list_1]
#print (list_3)


class Player:
    name = ""
    hp = 0
    dmg = 0
    def printPlayer(self):
        print ("name: " + self.name)
        print ("hp: " + str(self.hp))
        print ("dmg: " + str(self.dmg))

def printPlayer2(p):
            print ("name: " + p.name)
            print ("hp: " + str(p.hp))
            print ("dmg: " + str(p.dmg))
    

        

p1 = Player()
p2 = Player()

print (p1)
p1.name = "ted"
p1.dmg = 20
p1.hp = 100

p1.printPlayer()

printPlayer2(p1)


print (p2)
p2.name = "Jason"
p2.dmg = 20
p2.hp = 100

#players = (p1,p2)
#print (p1,p2)

#for p in players:
#    p.printPlayer()

