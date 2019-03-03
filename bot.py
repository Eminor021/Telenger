#!/usr/bin/python3

import Telibrary

bot = Telibrary.bot(str(), ### set the token of your bot instead of str(), you can see it in you bot settings.
                    str(), ### set your own chat id instead of str(), you can see your chat id by starting @userinfobot in telegram.
                    dict()) ### set your proxy instead of dict().

def Getit(Message):
    if Message['message']['text'] == '/start':
        bot.SendText(Message['message']['chat']['id'],
        'created by amoo amir.\nhttps://github.com/amooamirxd\nstart talking!',
        0,0,Message['message']['message_id'])
    elif Message['message']['text'][0] == '/':
        bot.SendText(Message['message']['chat']['id'],
        'DO NOT TRY TO SPAM! XD\n(messages shouldn\'t be started with "/" )',
        0,0,Message['message']['message_id'])
    else:
        bot.SendText(Message['message']['chat']['id'],
        'Sent! :)',
        0,0,Message['message']['message_id'])
        bot.Forward(bot.AdminID,
        Message['message']['chat']['id'],
        Message['message']['message_id'])

def TellAdmin(Text,ReplyToMessageID = 0):
    bot.SendText(bot.AdminID,Text,0,0,ReplyToMessageID)

def Bemessenger(Message):
    if Message['message']['from']['id'] == bot.AdminID and Message['message']['text'] == '/Help':
        TellAdmin('use /For to forward a message.',Message['message']['message_id'])
    else:
        bot.SendText(Message['message']['reply_to_message']['forward_from']['id'],
        Message['message']['text'])

updater = open('tmp.txt','r')
updateid = updater.readline()
updater.close()

while True:
    res = bot.Update(updateid)
    if res.json()['result'] != 0:
        for i in res.json()['result']:
            if i['message']['from']['id'] != int(bot.AdminID):
                Getit(i)
                updateid = i['update_id'] + 1
            else:
                try:
                    if i['message']['text'] == '/For':
                        TellAdmin('your next message will be forwarded to this user; /C to cancel!'
                        ,i['message']['reply_to_message']['message_id'])
                        updateid = i['update_id'] + 1
                        is_done = False
                        while not is_done:
                            tmp_res = bot.Update(updateid)
                            if tmp_res.json()['result'] != 0:
                                for j in tmp_res.json()['result']:
                                    if str(j['message']['from']['id']) != bot.AdminID:
                                        Getit(j)
                                        print(j)
                                        updateid = j['update_id'] + 1
                                    else:
                                        if j['message']['text'] == '/C':
                                            TellAdmin('cancelled!',j['message']['message_id'])
                                            updateid = j['update_id'] + 1
                                            is_done = True
                                        else:
                                            bot.Forward(i['message']['reply_to_message']['forward_from']['id'],bot.AdminID,j['message']['message_id'])
                                            updateid = j['update_id'] + 1
                                            TellAdmin('done!',j['message']['message_id'])
                                            updateid = j['update_id'] + 1
                                            is_done = True
                    elif i['message']['text'] == '/Help':
                        TellAdmin('reply a message to reply!\nuse /For to forward a message!')
                        updateid = i['update_id'] + 1
                    else:
                        Bemessenger(i)
                        updateid = i['update_id'] + 1
                except:
                    pass
            updater = open('tmp.txt','w')
            updater.writelines(str(updateid))
            updater.close()
