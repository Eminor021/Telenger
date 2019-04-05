import Telibrary
### to make a bot
import botlib
### to make it a messanger bot

### inintializing the bot:
bot = Telibrary.Bot(
    '', ### token
    '', ### owner's numerical ID
    {
        'https': 'socks5h://127.0.0.1:9050' ### proxy
    }
)

Messanger = botlib.MessengerBot(bot)

### I needed a tmp file to save the update id.
### give it the full path (pwd/tmp.txt)
updater = open('tmp.txt', 'r')
updateid = updater.readline()
updater.close()

def main(updateid):
    while True:
        res = bot.update(updateid)
        if res.json()['result'] != 0:
            for i in res.json()['result']:
                if i['message']['from']['id'] != int(bot.ADMINID):
                    Messanger.get_it(i)
                    updateid = i['update_id'] + 1
                else:
                    try:
                        if i['message']['text'] == '/For':
                            Messanger.tell_admin('your next message will be forwarded to this user; /C to cancel!',
                                    i['message']['reply_to_message']['message_id'])
                            updateid = i['update_id'] + 1
                            is_done = False
                            while not is_done:
                                tmp_res = bot.update(updateid)
                                if tmp_res.json()['result'] != 0:
                                    for j in tmp_res.json()['result']:
                                        if str(j['message']['from']['id']) != bot.ADMINID:
                                            messnger.get_it(j)
                                            print(j)
                                            updateid = j['update_id'] + 1
                                        else:
                                            if j['message']['text'] == '/C':
                                                Messanger.tell_admin('cancelled!', j['message']['message_id'])
                                                updateid = j['update_id'] + 1
                                                is_done = True
                                            else:
                                                bot.forward(i['message']['reply_to_message']['forward_from']['id'], 
                                                bot.ADMINID, 
                                                j['message']['message_id'])
                                                updateid = j['update_id'] + 1
                                                Messanger.tell_admin('done',
                                                j['message']['message_id'])
                                                updateid = j['updateid'] + 1
                        elif i['message']['text'] == '/Help':
                            Messanger.tell_admin('reply to reply and /For to forward!')
                            updateid = i['update_id'] + 1
                        else:
                            Messanger.send_it(i)
                            updateid = i['update_id'] + 1
                    except:
                        pass
### give it the full path (pwd/tmp.txt)
        updater = open('tmp.txt', 'w')
        updater.writelines(str(updateid))
        updater.close()

if __name__ == '__main__':
    main(updateid)
