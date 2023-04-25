class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        
    def addition(self):
        print(self.nombre1+ self.nombre2)

op1 = Operation(25, 3)
op1.addition()
