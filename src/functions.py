def retrieveForecast():
    import requests, ThreeDayPrediction, re

    request = requests.get("https://services.swpc.noaa.gov/text/3-day-forecast.txt")

    if request.status_code != requests.codes.ok:
        return "ERROR. Website not accessible"

    text = request.text.strip().split("\n")

    # Relevant times = [UTC 00-03, UTC 03-06, UTC 18-21, UTC 21-00]
    relevantTimes = [text[14], text[15], text[20], text[21]]
    KpIndexes = []
        
    for timeLine in relevantTimes:
        # Remove (G1) type of anomalies that happen when there is a solarstorm and all other non-necessary stuff
        stormForces = re.sub('\(.*\)|[0-9]{2}-[0-9]{2}UT|\s*', '', timeLine)
        KpIndexes.append(stormForces)
    forecast = ThreeDayPrediction.ThreeDayPrediction([int(x[0]) for x in KpIndexes], [int(x[1]) for x in KpIndexes], [int(x[2]) for x in KpIndexes])

    return forecast

def checkForecast(scheduler):
    import time
    forecast = retrieveForecast()
    message = forecast.analyzeForecasts()
    notify(message)

def notify(message):
    from win10toast import ToastNotifier
    import os, pathlib

    scriptPath = pathlib.Path(__file__).parent.absolute()
    imageFolderPath = os.path.join(scriptPath, '..', 'Images')
    toaster = ToastNotifier()

    if message == []:
        toaster.show_toast("Virmalisi pole :'( ", " ", 
        icon_path=os.path.join(imageFolderPath,'toastLogo.ico'), 
        threaded=True)

    else:
        longMessage = ""
        for text in message: longMessage += text + " || "
        toaster.show_toast("Virmaliste Hoiatus!\n" + longMessage, " ", 
        icon_path=os.path.join(imageFolderPath,'toastLogo.ico'), 
        threaded=True, duration=10)

def pause(scheduler):
    scheduler.pause()

def resume(scheduler):
    scheduler.resume()

#forc = retrieveForecast()
#msg, pos = forc.analyzeForecasts()
#print("msg", msg)
#print("pos", pos)