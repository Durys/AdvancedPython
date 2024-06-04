class Hour:

    def __init__(self, time):
        self._hour = time

    def return_hour(self):
        return str(self._hour)


class MinuteWrapper:

    def __init__(self, Hour):
        self.obj = Hour

    def return_hour(self):
        time = Hour.return_hour(self.obj)
        return str(time) + ":00"


class SecondWrapper:

    def __init__(self, Hour):
        self.obj = Hour

    def return_hour(self):
        time = Hour.return_hour(self.obj)
        return str(time) + ":00:00"


news = Hour(12)
now = news.return_hour()
print(now)

newer = MinuteWrapper(news)
now_minutes = newer.return_hour()
print(now_minutes)

newest = SecondWrapper(news)
now_seconds = newest.return_hour()
print(now_seconds)

