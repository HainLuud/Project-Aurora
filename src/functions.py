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

def checkForecast(scheduler):
    import time
    forecast = retrieveForecast()
    message, positiveForecast = forecast.analyzeForecasts()
    
    # If there is a positive forecast and the current time is past 6PM
    if positiveForecast and time.localtime()[3] > 18:
        # Should substitute with modifyable value
        scheduler.add_job(notify, 'interval', minutes=30, kwargs={"message":message}, id='positiveForecastJob')
    else:
        try:
            notify(message)
            scheduler.remove_job('positiveForecastJob')
        except:
            pass 

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
        longMessage = []
        for text in message: longMessage += text + "\n"
        toaster.show_toast("Virmaliste Hoiatus!", longMessage)

def pause(scheduler):
    scheduler.pause()

def resume(scheduler):
    scheduler.resume()

#Todo: Add load-configuration-file funcion, so that at startup your jobs, are all the same as you set them

