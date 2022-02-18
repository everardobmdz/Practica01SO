from Proceso import Proceso
class Lote():
    def __init__(self):
        self.procesos = []
        self.id = 0

    def getProcesos(self):
        return self.procesos
    
    def addProcess(self, pros):
        self.procesos.append(pros)

    def toString(self):
        text= ''
        for proceso in self.procesos:
            text += 'No. programa: ' + str(proceso.getId()) + '\nTiempo máximo: ' + str(proceso.getTime()) + '\n\n'

        return text
