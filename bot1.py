#!/usr/bin/env python3
from resources.credentials import bot_token, bot_user_name, chat_id
import requests

def send_to_telegram():
    import sys
    if  len( sys.argv ) < 1:
        message = input("give your message: ")
    else:
       message = sys.argv[1]
    apiURL = f'https://api.telegram.org/bot{bot_token}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chat_id, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)


if __name__ == "__main__":
   send_to_telegram()
