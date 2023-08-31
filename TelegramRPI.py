from sense_hat import SenseHat
import requests
from time import sleep
import matplotlib.pyplot as plt


# print(temp)


def telegram_bot_sendtext(bot_message):
    bot_token = ''
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)

    return response.json()


while True:
    sense = SenseHat()
    sense.clear()
    temp = round(sense.get_temperature())

    if temp > 20:
        temp_new = str(temp)
        test = telegram_bot_sendtext("!ATTENTIE! Temperatuur is: " + temp_new + " graden.")
        #test = telegram_bot_sendtext(temp_new)

        

        print(test)
        sleep(5)

        # value = 8
        # converted_value = str(value)
