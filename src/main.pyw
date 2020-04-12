import sys 
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt5.QtGui import QIcon
import ThreeDayPrediction
import time

def retrieveForecast():
    import requests, ThreeDayPrediction

    request = requests.get("https://services.swpc.noaa.gov/text/3-day-forecast.txt")

    if request.status_code != requests.codes.ok:
        return "ERROR. Website not accessible"

    text = request.text.strip().split("\n")

    # Relevant times = [UTC 00-03, UTC 03-06, UTC 18-21, UTC 21-00]
    relevantTimes = [text[14], text[15], text[20], text[21]]
    KpIndexes = []
    
    for timeLine in relevantTimes:
        KpIndexes.append(timeLine.replace(" ", "")[-3:])

    forecast = ThreeDayPrediction.ThreeDayPrediction([int(x[0]) for x in KpIndexes], [int(x[1]) for x in KpIndexes], [int(x[2]) for x in KpIndexes])

    return forecast

def notify(message):
    from win10toast import ToastNotifier
    toaster = ToastNotifier()

    if message == []:
        toaster.show_toast("Virmalisi pole :'( ", " ", 
        icon_path="Images\\toastLogo.ico", threaded=True)

    else:
        longMessage = []
        for text in message: longMessage += text + "\n"
        toaster.show_toast("Virmaliste Hoiatus!", longMessage)

def checkForecast(scheduler):
    forecast = retrieveForecast()
    message, positiveForecast = forecast.analyzeForecasts()

    # If there is a positive forecast and the current time is past 6PM
    if positiveForecast and time.localtime()[3] > 18:
        # Should substitute with modifyable value
        scheduler.add_job(notify, 'interval', minutes=30, kwargs={"message":message}, id='positiveForecastJob')
    else:
        try:
            scheduler.remove_job('positiveForecastJob')
        except:
            pass 


app = QApplication(sys.argv)

trayIcon = QSystemTrayIcon(QIcon('Images\\trayLogo.png'), parent=app)
trayIcon.setToolTip("Aurora Forecast")
trayIcon.show()

# Create menu
menu = QMenu()
exitAction = menu.addAction('Exit')
exitAction.triggered.connect(app.quit)

# Add right-click menu to systemtray icon
trayIcon.setContextMenu(menu)

# Make initial toast message
forecast = retrieveForecast()
message, positiveForecast = forecast.analyzeForecasts()
notify(message)

# Documentation: https://apscheduler.readthedocs.io/en/v3.6.3/index.html
from apscheduler.schedulers.background import BackgroundScheduler
scheduler = BackgroundScheduler()
scheduler.start()

# Every 45 minutes check the forecast
scheduler.add_job(checkForecast, 'interval', id="RegularCheck", minutes=30, kwargs={"scheduler":scheduler})

# Wait for app to say, that it wants to exit
sys.exit(app.exec_())