class ThreeDayPrediction:
  # forecastToday = [UTC 00-03, UTC 03-06, UTC 18-21, UTC 21-00]
  # forecastTomorrow = [UTC 00-03, UTC 03-06, UTC 18-21, UTC 21-00]
  # forecastTheDayAfterTomorrow = [UTC 00-03, UTC 03-06, UTC 18-21, UTC 21-00]

  def __init__(self, forecastToday, forecastTomorrow, forecastTheDayAfterTomorrow):
    self.forecastToday = forecastToday
    self.forecastTomorrow = forecastTomorrow
    self.forecastTheDayAfterTomorrow = forecastTheDayAfterTomorrow

  def analyzeForecasts(self):
    significanceThreshold = 5
    days = ["Täna ", "Homme ", "Ülehomme "]
    times = ["02:00 - 05:00", "05:00 - 08:00", "20:00 - 23:00", "23:00 - 02:00"]
    forecasts = [self.forecastToday, self.forecastTomorrow, self.forecastTheDayAfterTomorrow]
    message = []

    for i, forecast in enumerate(forecasts):

      for j in range(4):

        if forecast[j] >= significanceThreshold:
          message.append(days[i] + times[j] + " Tugevusega " + forecast[j])

    return message

