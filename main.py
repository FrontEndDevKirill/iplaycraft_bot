import telebot
import requests
import time

_token ='287585553:AAE5mxSyTKqVFZdmRUTCHs4dgZFYyiJ5m0w'
group_id = -74409254
vk_token="b64c2d4b4377f3574d55a161ecc2514af7500b9bf5f1c70a43a6fb86bfaa73be2fe81415f830cd1e5f167"

def main():
    bot = telebot.TeleBot(_token)
    r = requests.get('https://api.vk.com/method/wall.get', params={
        'owner_id': group_id,
        'offset': 0,
        'count': 1,
        'filter': "all",
        'access_token': vk_token,
        'v': 5.74
    })
    last_id = r.json()["response"]["items"][0]["id"]
    print("********* [ Начинаю мониторинг группы ] *********\n\n\n")
    while True:
        time.sleep(1)
        r = requests.get('https://api.vk.com/method/wall.get', params={
            'owner_id': group_id,
            'offset': 0,
            'count': 1,
            'filter': "all",
            'access_token': vk_token,
            'v': 5.74
        })
        if r.json()["response"]["items"][0]["id"] != last_id:
            print("*******Обнаружен новый пост в групе ВК")
            print("*******Отправляю сообщение в телеграмм ...")
            try:
                text = r.json()["response"]["items"][0]["text"]
                link = r.json()["response"]["items"][0]['attachments'][0]['photo']['photo_604']
                if len(text) <= 200:
                    bot.send_photo(-1001249278035, link, text)
                    last_id = r.json()["response"]["items"][0]["id"]
                    print("*******Сообщение успешно отправленно\n")
                else:
                    bot.send_photo(-1001249278035, link)
                    bot.send_message(-1001249278035, text)
                    last_id = r.json()["response"]["items"][0]["id"]
                    print("*******Сообщение успешно отправленно\n")
            except KeyError:
                text = r.json()["response"]["items"][0]["text"]
                bot.send_message(-1001249278035, text)
                last_id = r.json()["response"]["items"][0]["id"]
                print("*******Сообщение успешно отправленно\n")
        # else:
        #     print(last_id)


if __name__ == '__main__':
    main()



