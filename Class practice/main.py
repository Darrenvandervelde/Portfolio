class strongCharacter:
    def __init__(self, name, gender, race):
        self.name = name
        self.gender = gender
        self.race = race
        self.lv = 1
        self.xp = 0
        self.atk = 7
        self.deff = 7
        self.intel = 4
         
    def add_xp(self, added_xp):
         self.xp = self.xp + int(added_xp)
         while self.xp >= 100:
              self.lv += 1
              self.atk += 1
              self.deff += 1.5
              self.intel += 0.5
              self.xp -= 100
              print("You Levelled up!!!")

class smartCharacter:
    def __init__(self, name, gender, race):
            self.name = name
            self.gender = gender
            self.race = race
            self.lv = 1
            self.xp = 0
            self.atk = 7
            self.deff = 4
            self.intel = 8

    def add_xp(self, added_xp):
             self.xp = self.xp + int(added_xp)
             while self.xp >= 100:
                  self.lv += 1
                  self.atk += 1
                  self.deff += 0.5
                  self.intel += 1.5
                  self.xp -= 100
                  print("You Levelled up!!!")
    

class nimbleCharacter:
    def __init__(self, name, gender, race):
            self.name = name
            self.gender = gender
            self.race = race
            self.lv = 1
            self.xp = 0
            self.atk = 8
            self.deff = 4
            self.intel = 6

    def add_xp(self, added_xp):
             self.xp = self.xp + int(added_xp)
             while self.xp >= 100:
                  self.lv += 1
                  self.atk += 1.5
                  self.deff += 0.5
                  self.intel += 1
                  self.xp -= 100
                  print("You Levelled up!!!")
        

def start():
      
    print("Welcome to Ilandia!")
    print("_____________________________")
    print("What would you like your character to be called?")
    name = input(">>>")
    print("What would you like their race to be?")
    race = input(">>>")
    print("What would you like their gender to be?")
    gender = input(">>>")
    complete = False
    while complete == False:
        print("Would you like them to be strong, nimble, or smart?")
        type = input(">>>")
        complete = True
        if type == "strong":
            yourCharacter = strongCharacter(name, gender, race)
        elif type == "smart":
            yourCharacter = smartCharacter(name, gender, race)
        elif type == "nimble":
            yourCharacter = nimbleCharacter(name, gender, race)
        else:
            complete = False
            print("You entered something wrong, try again")
         
    
    print("Ok we're all set to go!")
    return yourCharacter


def menu(yourCharacter):
    still_playing = True
    
    while still_playing == True:

        print("_____________________________")
        print(f"Name: {yourCharacter.name}  Gender: {yourCharacter.gender}  Race: {yourCharacter.race}")#
        print(f"Level: {yourCharacter.lv}  EXP: {yourCharacter.xp}  Attack: {yourCharacter.atk}  Defence: {yourCharacter.deff}  Intelligence: {yourCharacter.intel}")
        print("What would you like to do next?")
        print("You can:")
        print("(A)Add xp")
        print("(B)Quit")
        choice = input(">>>")

        if choice == "A":
            print("How much xp would you like to add?")
            yourCharacter.add_xp(input(">>>"))
        elif choice == "B":
            still_playing = False
            print("_____________________________")
            print("We'll miss you! Come back again sometime")
        else:
             print("You input an incorrect option. Try again")


yourCharacter = start()
menu(yourCharacter)