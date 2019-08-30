#################### Imports #######################

#Imports das UI's
from Ui_logged import *
from resources_mat_rc import *

#Imports das bibliotecas: geral
from PyQt5.QtCore import *
import time
import platform
import sys

####################### End of Imports ########################

   
class ThreadSignal(QObject): 
        sig = pyqtSignal(str) 

class webThread(QThread): #Thread de leitura dos crachás
    send2thread_signal = ThreadSignal()

    def signal_test(self, url):
        print('sinal emitido')
        self.signal_login.emit(url) 
    
    def run(self):
        global logged
        global objLogged

        while(True):
                link ='https://www.google.com.br'
                self.send2thread_signal.sig.emit(str(link))
                time.sleep(10)
                link ='https://www.github.com'
                self.send2thread_signal.sig.emit(str(link))
                time.sleep(10)
                link ='https://www.twitter.com'
                self.send2thread_signal.sig.emit(str(link))
                time.sleep(10)



   

#Classe que herda as propriedades da classe Ui_Logged e gerencia a formação e os eventos da janela inicial
class Logged(QtWidgets.QMainWindow, Ui_Logged):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.thread = webThread()
        self.thread.send2thread_signal.sig.connect(self.load_url)
                
    def load_url(self, url):
        self.web.setUrl(QUrl(url))




#Função principal que inicia as funcionalidades e o programa
def main():
        app = QtWidgets.QApplication([])

        global logged
        logged = QtWidgets.QMainWindow()
        global objLogged
        objLogged = Logged()
        objLogged.setupUi(logged)        
        logged.show()

        thread = webThread()
        thread.start()

        app.exec_() #loop principal de excução da GUI
        thread.terminate() #fim da thread com o fim do programa (apenas prevenção, não se espera que o programa termine)

if __name__ == "__main__":
        main()

