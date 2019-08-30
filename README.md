# Qt5-Webview-on-a-Raspberry-Pi
Tutorial code about the usage and instalation of QtWebKit in a PyQt5 app running on a Raspberry Pi (probably working in any armhf device)

![alt text](https://media.licdn.com/dms/image/C4D0BAQFopxfUB5xTZw/company-logo_200_200/0?e=2159024400&v=beta&t=af-X8cgb9ZecB_Z9bcskiikUkdLlEwLx4l00q2IDQj4) 

## Definition
PyQt5 is a GUI Python framework that works fine in almost every situation and device. __Almost__. Showing a web viewer inside your code can be a necessity sometimes, and with the "brand new" [QWebEngine](https://wiki.qt.io/QtWebEngine "QWebEngine reference") we have a powerfull and easy way to insert a webviewer in our applications.

The problem is: armhf devices do not support QWebEngine yet, so is it impossible to run a webviewer in a Raspberry Pi based app?

The short answer: No, It's possible!


The long answer: Oh god why no one makes a good tutorial teaching how to make it easily?

## Solutions
Counterpointing QWebEngine, we have the deprecated and __misterious__ [QtWebKit](https://wiki.qt.io/Qt_WebKit "QtWebkit reference"), the QWebKit turned deprecated at Qt 5.5, but it still possible to use it if you download the packages... And the best part: __It works in armhf based devices__.

## Setup
Well, first, you need a Raspberry Pi. I used a model 3B+. Follow this [tutorial](https://www.raspberrypi.org/downloads/noobs/ "Noobs reference") to setup a ready-to-work Raspbian Raspberry Pi. 

Then to run our code, you need to download PyQt5 and all the packages that you'll need using the following commands:
```
sudo apt-get install python3-pyqt5
sudo apt-get install python3-pyqt5.webkit
sudo apt-get install python3-pyqt5.svg
```
## Explaining the code
Well, in this example, I used QtDesigner (that you can download for Windows [here](https://build-system.fman.io/qt-designer-download "Portable QtDesigner"))
You can watch some tutorials [here](https://www.youtube.com/watch?v=LYF0spYkXUs "QtDesigner tutorial video") and you'll build your GUI (I recommend you to use my UI file inside the __/uis__ folder).
You probbably will notice that is __impossible__ to add a QWebView widget in the QtDesigner. But to overcome this problem, I use a hint. 
1. Build your Main Window
2. Setup inside your Window a __QGraphicsView__ widget in the place that you want your webviewer.
3. Save your UI file
4. Compile it in a __.py__ file

After that, we will edit the compiled-to-python UI file (I know that this is not practical, but It works).
Please open yout compiled UI file in your favorite text editor and follow this steps:

1. Add these imports to the file: (pay attention, do __not__ delete any original import)

```python
from PyQt5.QtWebKitWidgets import *
import sip
from PyQt5.QtCore import QUrl
from PyQt5.QtWebKit import *
from PyQt5.QtNetwork import *
```
2. Search your QwebGraphics object declaration and switch it to a QWebView object declaration:

__before:__
```python
        self.web = QGraphicsView(self.centralwidget)
        self.web.setGeometry(QtCore.QRect(361, 51, 1011, 721))
        self.web.setObjectName("web")
```
__after:__
```python
        self.web = QWebView(self.centralwidget)
        self.web.setGeometry(QtCore.QRect(361, 51, 1011, 721))
        self.web.setObjectName("web")
```

Now you can focuses on your main code ;)

## Additional information
The main code working with the compiled UI file is a full working example of how to run a window built with the designer, how to use a Qthread, how to setup signals and slots, how to change the UI view from inside the Qthread, and the __most__ hard thing with almost 0 documentation on internet: __how to use all this things together to change the URL of your webviewer while your program runs__.

Please pay attention to the main code example, and try to learn the things that I've said before (if you're in the right way, you'll need this information soon)

__Important__: just the UI.py file can't be executed. The main.py file should be runned to execute this program. 

__Some good explanation__:
The main.py program is an example of how to change the QWebView url from a QThread, (it actually just open one different website each 10 seconds (Google or Github or Twitter)

