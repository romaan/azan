#!/usr/bin/python

import schedule
import time
from datetime import date
import os
from prayer_time import prayTimes

def job(minute, hour, command):
  os.system("""(crontab -u romaan -l ; echo "{} {} * * * {}") | crontab -u romaan - """.format(minute, hour, command))

if __name__ == '__main__':
  # Calculate prayer times for the day and schedule
  os.system("crontab -r")
  prayer_times = prayTimes.getTimes(date.today(), (-27.46, 153.02), 10)
  job(0, 1, "/home/romaan/azan/run.py")
  for i in ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']:
    hour, minute = str(prayer_times[i.lower()]).split(":")
    job(minute, hour, "/usr/bin/omxplayer /home/romaan/azan/1.mp3")
