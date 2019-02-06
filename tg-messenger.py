#!/usr/bin/python3
import requests
from time import sleep

session = requests.session()
session.proxies = dict() ### proxy ( optional )

API_TOKEN = str() ### token of the bot
AdminID = str() ### chat ID
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
                        if i['message']['text'] == '/f':
                            msgtmp = 'I\'ll forward the next message to this user! /c to cancel the operation!'
                            COMMAND = 'sendmessage'
                            session.post('https://api.telegram.org/bot%s/%s?chat_id=%s&text=%s&reply_to_message_id=%s'%(API_TOKEN, COMMAND,
                            AdminID,msgtmp,
                            (i['message']['reply_to_message']['message_id'])
                            ),
                            proxies = session.proxies,
                            )
                            ChatIdTemp = i['message']['reply_to_message']['forward_from']['id']
                            dntemp = False
                            while not dntemp:
                                COMMAND = 'getupdates?offset=%s' % str(UID+2)
                                RESPONSE = session.get('https://api.telegram.org/bot%s/%s'%(API_TOKEN,COMMAND), proxies = session.proxies)
                                for j in RESPONSE.json()['result']:
                                    if j['message']['from']['id'] == int(AdminID):
                                        if j['message']['text'] == '/c':
                                            dntemp = True
                                            COMMAND = 'sendmessage'
                                            session.post('https://api.telegram.org/bot%s/%s?chat_id=%s&text=cancelled+:\&reply_to_message_id=%s'%(API_TOKEN, COMMAND,
                                            AdminID,
                                            (j['message']['message_id'])
                                            ),
                                            proxies = session.proxies,
                                            )
                                        else:
                                            COMMAND = 'forwardMessage'
                                            session.post('https://api.telegram.org/bot%s/%s?chat_id=%s&from_chat_id=%s&message_id=%s'%(API_TOKEN,COMMAND,
                                            ChatIdTemp,AdminID,
                                            (j['message']['message_id'])
                                            ),
                                            proxies = session.proxies,
                                            )
                                            dntemp = True
                                            COMMAND = 'sendmessage'
                                            session.post('https://api.telegram.org/bot%s/%s?chat_id=%s&text=done+:)&reply_to_message_id=%s'%(API_TOKEN, COMMAND,
                                            AdminID,
                                            (j['message']['message_id'])
                                            ),
                                            proxies = session.proxies,
                                            )
                                            break
                        else:
                            try:
                                COMMAND = 'sendmessage'
                                session.post('https://api.telegram.org/bot%s/%s?chat_id=%s&text=%s'%(API_TOKEN, COMMAND,
                                (i['message']['reply_to_message']['forward_from']['id']),
                                (i['message']['text']),
                                ),
                                proxies = session.proxies,
                                )
                            except:
                                pass
                    except:
                        pass
            else:
                if i['message']['text'] == '/start':
                    msgtmp = 'created by pino.\nhttps://github.com/PinoQxD\nleave your message!'
                    COMMAND = 'sendmessage'
                    session.post('https://api.telegram.org/bot%s/%s?chat_id=%s&text=%s&s&reply_to_message_id=%s'%(API_TOKEN, COMMAND,
                    (i['message']['chat']['id']),
                    msgtmp,
                    (i['message']['message_id'])
                    ),
                    proxies = session.proxies,
                    )
                elif i['message']['text'][0] == '/':
                    pass
                else:
                    COMMAND = 'sendmessage'
                    session.post('https://api.telegram.org/bot%s/%s?chat_id=%s&text=sent+:)&reply_to_message_id=%s'%(API_TOKEN, COMMAND,
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
