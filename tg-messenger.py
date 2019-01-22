#!/usr/bin/python3
import requests
from time import sleep

session = requests.session()
session.proxies = dict() ### proxy ( optional )

API_TOKEN = str() ### token of the bot
AdminID = str() ### caht ID
UID = int()
while True:
    UpLis = open('tmp.txt','r') 
    UID = int(UpLis.readline())
    COMMAND = 'getupdates?offset=%s' % str(UID+1)
    RESPONSE = session.get('https://api.telegram.org/bot%s/%s'%(API_TOKEN,COMMAND), proxies = session.proxies)
    if len(RESPONSE.json()['result']) != 0:
        for i in RESPONSE.json()['result']:
            if i['message']['from']['id'] == int(AdminID):
                try:
                    COMMAND = 'forwardMessage'
                    session.post('https://api.telegram.org/bot%s/%s?chat_id=%s&from_chat_id=%s&message_id=%s'%(API_TOKEN,COMMAND,
                    (i['message']['reply_to_message']['forward_from']['id']),
                    (i['message']['chat']['id']),
                    (i['message']['message_id'])
                    ),
                    proxies = session.proxies,
                    )
                except:
                    pass
            else:
                COMMAND = 'sendmessage'
                session.post('https://api.telegram.org/bot%s/%s?chat_id=%s&text=Sent!+:)&reply_to_message_id=%s'%(API_TOKEN, COMMAND,
                (i['message']['chat']['id']),
                (i['message']['message_id'])
                ),
                proxies = session.proxies,
                )
                COMMAND = 'forwardMessage'
                session.post('https://api.telegram.org/bot%s/%s?chat_id=%s&from_chat_id=%s&message_id=%s'%(API_TOKEN,COMMAND,
                AdminID,
                (i['message']['chat']['id']),
                (i['message']['message_id'])
                ),
                proxies = session.proxies,
                )
            UID = int(i['update_id'])
    UpLis.close()
    UpLis = open('tmp.txt','w')
    UpLis.writelines(str(UID))
    UpLis.close()
    sleep(2)
