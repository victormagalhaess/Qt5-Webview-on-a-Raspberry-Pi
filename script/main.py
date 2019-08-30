#################### Imports #######################

#Imports das UI's
from Ui_logged import *
from PyQt5.QtCore import *
import time
import platform
import sys
   
class ThreadSignal(QObject): #Signal class (you better use it on your code)
        sig = pyqtSignal(str) 
      

class webThread(QThread): 
    send2thread_signal = ThreadSignal()
      
    
    def run(self):
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
                  

#Class to generate the main Window
class Logged(QtWidgets.QMainWindow, Ui_Logged):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.thread = webThread()
        self.thread.send2thread_signal.sig.connect(self.load_url)
                
    def load_url(self, url):
        self.web.setUrl(QUrl(url))
         

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
        app.exec_() #GUI main loop
        thread.terminate() #thread end

      
if __name__ == "__main__":
        main()

