class Syra_Object :
    def __init__ (self):
        pass
        with open ("entree.txt", "r+") as file:
            chiffre = file.read()
        
        self.u = int(chiffre)

    def syracuse (self):
        while (self.u != 1):
            if (self.u % 2 == 0 and self.u > 0):
                self.u = self.u//2
                print(self.u)
            elif (self.u % 2 == 1 and self.u > 0):

                self.u = self.u*3 + 1
                print(self.u)


v = Syra_Object()
v.syracuse()