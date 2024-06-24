import datetime
from requests_html import HTMLSession
import json, win32api

Session = HTMLSession()
timezoneInfo = json.loads(Session.get("https://worldtimeapi.org/api/timezone/Etc/GMT").content)
day_of_week =int(timezoneInfo['day_of_week'])
timeIso=datetime.datetime.fromisoformat(timezoneInfo['datetime'])
win32api.SetSystemTime(int(timeIso.year)
                       ,timeIso.month
                       ,day_of_week
                       ,timeIso.day,timeIso.hour,timeIso.minute,timeIso.second,int(timeIso.microsecond/1000))
