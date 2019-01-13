#!/usr/bin/python3
import requests
from time import sleep

session = requests.session()
session.proxies = { 
                  }
### set the proxy ( optional )
API_TOKEN = ''
### set your token
UID = int()
while True:
    UpLis = open('file','r')
    ### open the .txt file
    UID = int(UpLis.readline())
    COMMAND = 'getupdates?offset=%s' % str(UID+1)
    RESPONSE = session.get('https://api.telegram.org/bot%s/%s'%(API_TOKEN,COMMAND), proxies = session.proxies)
    if len(RESPONSE.json()['result']) != 0:
        COMMAND = 'sendmessage'
        for i in range(len(RESPONSE.json()['result'])):
            session.post('https://api.telegram.org/bot%s/%s?chat_id=%s&text=Sent!+:)&reply_to_message_id=%s'%(API_TOKEN, COMMAND,
            (RESPONSE.json()['result'][i]['message']['chat']['id']),
            (RESPONSE.json()['result'][i]['message']['message_id'])
            ),
            proxies = session.proxies,
            )
            COMMAND = 'forwardMessage'
            session.post('https://api.telegram.org/bot%s/%s?chat_id=
            ### erase this whole line and write your nimberical ID! ( get your numberical id using 'userinfobot' )
            &from_chat_id=%s&message_id=%s'%(API_TOKEN,COMMAND,
            (RESPONSE.json()['result'][i]['message']['chat']['id']),
            (RESPONSE.json()['result'][i]['message']['message_id'])
            ),
            proxies = session.proxies,
            )
            UID = int(RESPONSE.json()['result'][i]['update_id'])
    UpLis.close()
    UpLis = open('/home/pinocchio/Documents/PinoPy/mrpinotmp.txt','w')
    UpLis.writelines(str(UID))
    UpLis.close()
    sleep(2)
