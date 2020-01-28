import ThreeDayPrediction

def webscrape():
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
        toaster.show_toast("Virmalisi pole :'( ", " ")

    else:
        longMessage = []
        for text in message: longMessage += text + "\n"
        toaster.show_toast("Virmaliste Hoiatus!", longMessage)

from apscheduler.schedulers.blocking import BlockingScheduler

blockScheduler = BlockingScheduler()

# A scheduled job that runs every day at 19:00
@blockScheduler.scheduled_job('cron', day_of_week='mon-sun', hour=19)
def scheduled_job():
    forecast = webscrape()
    message = forecast.analyzeForecasts()
    notify(message)

@blockScheduler.scheduled_job('cron', day_of_week='mon-sun', hour=9)
def scheduled_job2():
    forecast = webscrape()
    message = forecast.analyzeForecasts()
    notify(message)

blockScheduler.start()

