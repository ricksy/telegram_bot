#!/usr/bin/env python3
from time import sleep
#from resources.credentials import bot_token, bot_user_name, chat_id
import requests
import sys
import os
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
bot_token = os.environ.get('BOT_TOKEN')
bot_user_name = os.environ.get('BOT_USER_NAME')
chat_id = os.environ.get('CHAT_ID')

def send_to_telegram(message):
    apiURL = f'https://api.telegram.org/bot{bot_token}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chat_id, 'text': f'{datetime.now()}: ' + message})
        print(response.text)
    except Exception as e:
        print(e)
interval = 10
if __name__ == "__main__":
    message = "Starting bot"
    send_to_telegram(message)
    # Creates a default Background Scheduler
    sched = BackgroundScheduler()
    # Schedule job_function to be called every 30 minutes
    sched.add_job(send_to_telegram, 'interval', seconds=interval,
                        args=['Go for a walk now!'])
    sched.start()
    while True:
        sleep(interval)
    
