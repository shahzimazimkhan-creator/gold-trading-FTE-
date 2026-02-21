import schedule
import time
from app import run_fte

schedule.every(15).minutes.do(run_fte)

while True:
    schedule.run_pending()
    time.sleep(1)
