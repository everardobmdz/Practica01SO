

class lote():
    def __init__(self):
        self.procesos = []



class Main():
    def __init__(self):
        self.cola = []

        self.actualLot = lote()


    def addProcess(self):
        self.actualLot.procesos.append(1)
        self.actualLot.procesos.append(2)
        self.actualLot.procesos.append(3)

        self.cola.append(self.actualLot)
        print(self.cola[0].procesos)
        self.actualLot = lote()
        self.actualLot.procesos.append(4)
        print(self.cola[0].procesos)
        self.cola.append(self.actualLot)
        print(self.cola[0].procesos)
        print(self.cola[1].procesos)

prueba = Main()

prueba.addProcess()