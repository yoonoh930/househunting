# -*- coding: utf-8 -*-
"""House Hunter

This app is designed to make house hunting easier for Lea.

Example:





Written: 1/12/2018
Last Updated: 1/12/2018
"""

import requests
import datetime

TOKEN = 548727415:AAEvilyCpc4JO-8ABc0AzVtcj7fJs-ZLQiU

class HouseHunter:
    """The bot that collects new posts on houses in France

    Attributes:
        token (str): The token to access the telegram bot.
        api_url (str): The url to request api access.

    """

    def __init__(self, token):
        """__init__ method to instanciate api request object for telegram chatbot"""

        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        """The method to get updates from telegram server

        Args:
            offset: To indicate certain updates have been seen
            timeout: The seconds the scrip will take before getting other updates?

        Returns:
            json result file which includes message_id, from, chat

        """
        method = 'getUpdates'
        params = { 'timeout': timeout, 'offset': offset }
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json


    def send_messages(self, chat_id, text):
        """The method to send message to the chat through a telegram server

        Args:
            chat_id: The chat room id
            text: The text to be sent

        Returns:
            requests.post
        """
        params = { 'chat_id': chat_id, 'text': text}
        method = 'sendMessages'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_updates(self):
        """ The method to get the last result

        Returns:
            last_update
        """
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update


hunter_Bot = HouseHunter(TOKEN)
greeting = ('hello', 'hi', 'greeting', 'sup')
now = datetime.datetime.now()

def main():
    new_offset = None
    today = now.day
    hour = now.hour

    while True:
        hunter_Bot.get_updates(new_offset)

        last_update = hunter_Bot.get_last_updates()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
            greet_bot.send_message(last_chat_id, 'Good Morning  {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
            greet_bot.send_message(last_chat_id, 'Good Afternoon {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
            greet_bot.send_message(last_chat_id, 'Good Evening  {}'.format(last_chat_name))
            today += 1

        new_offset = last_update_id + 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
