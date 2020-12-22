import os, sys, pathlib, functions, ctypes
import Logic

# Tell WIndows, that this .pyw is hosting other applications and is not an application in itselt 
# (a workaround to get the Window icon to display correctly)
myappid = u'HainProductions.AuroraForecaster.vestion=1.1' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

scriptPath = pathlib.Path(__file__).parent.absolute()
imageFolderPath = os.path.join(scriptPath, '..', 'Images')

# Make initial toast message
forecast = functions.retrieveForecast()
message = forecast.analyzeForecasts()
functions.notify(message)

from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import Ui_MainWindow

logic = Logic.Logic()

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self, logic)

class TrayWidget(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)

        # Add right-click menu for tray icon
        menu = QtWidgets.QMenu(parent)
        resumeAction = menu.addAction("Resume")
        resumeAction.triggered.connect(lambda: functions.resume(logic.scheduler))
        pauseAction = menu.addAction("Pause")
        pauseAction.triggered.connect(lambda: functions.pause(logic.scheduler))
        exitAction = menu.addAction("Exit")
        exitAction.triggered.connect(app.quit)

        self.setContextMenu(menu)
        self.setToolTip("Aurora Forecast")
    
        # Add left-click on icon -> MainWindow open action
        self.activated.connect(self.launchWindow)
        

    def launchWindow(self, reason):
        if reason == self.Trigger:
            self.window = MainWindow()
            self.window.setWindowTitle("Aurora Forecast Logic")
            self.window.show()
            
app = QtWidgets.QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)
app.setWindowIcon(QtGui.QIcon(os.path.join(imageFolderPath,'trayLogo.png')))
w = QtWidgets.QWidget()
tray_widget = TrayWidget(QtGui.QIcon(os.path.join(imageFolderPath,'trayLogo.png')), w)
tray_widget.show()

# Wait for app to say, that it wants to exit
sys.exit(app.exec_())