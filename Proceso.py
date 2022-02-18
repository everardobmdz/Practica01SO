import time
class Proceso():
    def __init__(self,name, operation, time, id, op1, op2):
        self.name = name
        self.operation = operation
        self.time = time
        self.result = 0
        self.id = id

        self.op1 = op1
        self.op2 = op2


    def getName(self):
        return self.name
    def getOperation(self):
        return self.operation
    def getTime(self):
        return self.time
    def getResult(self):
        return self.result  
    def getId(self):
        return self.id          


    def subTime(self):
        self.time = self.time -1
    
    def makeOperation(self):
        self.op1 = int(self.op1)
        self.op2 = int(self.op2)
        
        if self.operation == '+':
            self.result = self.op1 + self.op2
        elif self.operation == '-':
            self.result = self.op1 - self.op2
        elif self.operation == '*':
            self.result = self.op1 * self.op2
        elif self.operation == '/':
            try:
                self.result = self.op1 / self.op2
            except:
                print("error en la división")
        elif self.operation == 'Potencia':
            self.result = self.op1**self.op2
        elif self.operation == 'Residuo':
            self.result = self.op1 % self.op2

    def toString(self):
        text = 'Nombre de programador: ' + self.name + '\n' + 'Operación: ' + str(self.op1) + ' ' + self.operation + ' ' + str(self.op2) + '\n' + 'Tiempo máximo: ' + str(self.time) + 'segs\n' + 'No. de programa: ' + str(self.id)
        return text
    def finishedString(self):
        text = 'No. programa: ' + str(self.id) + '\nOperación: ' + str(self.op1) + ' ' + self.operation + ' ' + str(self.op2) + '\nResultado: ' + str(self.result) 
        return text