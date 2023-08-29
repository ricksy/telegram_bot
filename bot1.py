#!/usr/bin/env python3
from time import sleep
from resources.credentials import bot_token, bot_user_name, chat_id
import requests
import sys
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BlockingScheduler

def send_to_telegram(message):
    apiURL = f'https://api.telegram.org/bot{bot_token}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chat_id, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    if  len( sys.argv ) < 2:
        message = input("give your message: ")
    else:
        message = sys.argv[1]
    send_to_telegram(message)
    # Creates a default Background Scheduler
    sched = BlockingScheduler()
    exec_date = now_plus_10 = datetime.now() + timedelta(seconds = 5)
    #job = sched.add_date_job(send_to_telegram, exec_date, ['this is a scheduled message'])
    sched.add_job(send_to_telegram, 'date', run_date = exec_date,
                           args=['Job 1'])
    sched.start()
    print("Job scheduled at: ", exec_date)
    while True:
        sleep(1)
    
