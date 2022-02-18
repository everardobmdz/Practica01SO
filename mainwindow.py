from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from ui_mainwindow import Ui_MainWindow
from PySide2.QtCore import Slot, QTimer
from datetime import datetime
import time
from Lote import Lote
from Proceso import Proceso
import threading

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        self.queue = []
        self.actualLot = Lote()
        
        self.cont = 0
        self.contLots = 0

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.threads = []
        

        #Cronometro
        self.timer = QTimer(self) 
        self.count = 1
        self.flag = False

        self.timer.timeout.connect(self.showTime) 
        self.threads.append(self.timer)
        #self.timer.start(100)

        self.startTime = 0


        self.ui.addButton.clicked.connect(self.startAddProcess)
        self.ui.startButton.clicked.connect(self.start)

        self.t2 = threading.Thread(target=self.execution)
        self.threads.append(self.t2)
    
    @Slot()
    def startAddProcess(self):
        processAdd = threading.Thread(target=self.addProcess)
        self.threads.append(processAdd)
        processAdd.start()
    
    def addProcess(self):
        name = self.ui.nameProgrammer.text()
        op1 = int(self.ui.op1.text())
        op2 = int(self.ui.op2.text())
        operator = self.ui.operation.currentText()
        time = int(self.ui.maxTime.value())
        id = self.cont
        process = Proceso(name, operator, time, id, op1, op2)

        self.cont += 1

        if len(self.queue) == 0:
            self.queue.append(self.actualLot)

        if len(self.actualLot.getProcesos()) < 4:
            self.actualLot.addProcess(process)
        else:
                self.actualLot.setId = len(self.queue)+1
                self.queue.append(self.actualLot)
                self.actualLot = Lote()
                self.actualLot.addProcess(process)
        self.ui.nameProgrammer.clear()
        self.ui.op1.clear()
        self.ui.op2.clear()
        self.ui.maxTime.clear()
        self.ui.numProgram.setValue(self.cont)
        

    @Slot()
    def start(self):
        self.startTime = datetime.now()
        self.flag = True
        process = threading.Thread(target=self.execution)
        timeProcess = threading.Thread(target=self.setTime)
        self.threads.append(timeProcess)
        self.threads.append(process)
        timeProcess.start()
        process.start()
        #self.timer.start(100)
        
    def execution(self):
        cont = 0
        self.contLots = len(self.queue)
        self.ui.pendingLots.setText(str(self.contLots))
        lotCopy = Lote()
        for lot in self.queue:
            #lotCopy = lot.copy()
            self.ui.finishedBox.insertPlainText('\n-----Lote '+str(cont) + '------\n')
            for process in lot.procesos:
                self.ui.inEjecutionLotBox.clear()
                self.ui.inEjecutionLotBox.insertPlainText(lot.toString())
                self.ui.inEjecutionBox.clear()
                process.makeOperation()
                processTime = process.getTime()
                self.ui.inEjecutionBox.insertPlainText(process.toString())
                for i in range(processTime):
                    processTimeLeft = processTime - i
                    self.ui.processTime.setText(str(i+1))
                    self.ui.processTimeLeft.setText(str(processTimeLeft))
                    time.sleep(1)
                self.ui.finishedBox.insertPlainText(process.finishedString()+'\n\n')
                #lotCopy.procesos.pop(0)
            cont += 1
            self.contLots -= 1
            self.ui.pendingLots.setText(str(self.contLots))
        self.flag = False

    def cronometro(self):
        seconds = (datetime.now() - self.startTime).total_seconds()
        return self.formatTime(int(seconds))

    def formatTime(self, seconds):
        hours = int(seconds / 60 / 60)
        seconds -= hours*60*60
        minutos = int(hours/60)
        seconds -= minutos*60
        return f"{hours:02d}:{minutos:02d}:{seconds:02d}"

    def setTime(self):
        print("Refrescando!")

        formatTime = self.cronometro()
        self.ui.clock.setText(formatTime)
        time.sleep(0.5)
        if self.flag:
            self.setTime()
        return

    def showTime(self): 
        if self.flag: 
            self.count+= 1
        

        seconds = int(self.count / 10)
        text = self.formatTime(seconds)
        
        self.ui.clock.setText(text)


  
    def Pause(self): 
  
        self.flag = False
  

        
        

       
     
