# # 2 Create 5 classes of your choice and write mimimuum 2 attribute and 1 method  in each class.

class Beautician:
    def __init__(self, Lipstick, Eyeliner):
        self.Lipstick = Lipstick
        self.Eyeliner = Eyeliner

    def display(self):
        print( self.Lipstick, self.Eyeliner)

B1 = Beautician("loreal lipstick","dazzler eterna")
B2 = Beautician("matte lipstick","heaven eyeliner")
print(B1.Lipstick)

B1.display()
B2.display()



class Saloon:
    def __init__(self,Facepack,Facial):
        self.Facepack = Facepack 
        self.Facial = Facial
    def display_details(self):
        print(self.Facepack,self.Facial)
B1 = Saloon("Dtan","Brightning")
B2 = Saloon("O3","Shahnaj")

print(B1.Facepack)
B1.display_details()
B2.display_details()


class Bag:
    def __init__(self,suitcase,handbag):
        self.suitcases = suitcase
        self.Handbag = handbag
    def display_details(self):
        print(self.suitcases,self.Handbag)
B1 = Bag("Samsonite","Delsey Paris")
B2 = Bag("Louis Vuitton","Baggit")

print(B1.suitcases)
B1.display_details()
B2.display_details()

class Electricshop:
    def __init__(self, Fan, WashingMachine):
        self.Fan = Fan
        self. WashingMachine =  WashingMachine
    def display_details(self):
        print(self. Fan,self.WashingMachine)
B1 = Electricshop("Orient","Bajaj")
B2 = Electricshop("Haier","Samsung")

print(B1.Fan)
B1.display_details()
B2.display_details()

class Cloths:
    def __init__(self, Jeans, Shirt ):
        self.Jeans = Jeans
        self. Shirt =  Shirt
    def display_details(self):
        print(self. Jeans,self.Shirt)
B1 = Cloths("Zara","H&M")
B2 = Cloths("Raymond","Tommy Hilfiger")

print(B1.Jeans)
B1.display_details()
B2.display_details()








    
    

