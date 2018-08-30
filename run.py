#!/usr/bin/python

import schedule
import time
from datetime import date
import os

from prayer_time import prayTimes
def job():
  os.system("/usr/bin/omxplayer /home/romaan/azan/1.mp3")

if __name__ == '__main__':
  # Calculate prayer times for the day and schedule
  prayer_times = prayTimes.getTimes(date.today(), (-27.46, 153.02), 10)
  for i in ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']:
    schedule.every().day.at(str(prayer_times[i.lower()])).do(job)
  while True:
    schedule.run_pending()
    time.sleep(60)
