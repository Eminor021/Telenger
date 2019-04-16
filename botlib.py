import Telibrary

class MessengerBot(object):

### we have to have a bot to make it a messenger bot!
        def __init__(self, bot):
                self._bot = bot

        @property
        def BOT(self):
                return self._bot

### when a user sends a message to the bot, it has to show you the message!
        def get_it(self, Message):
### starting the bot
                if Message['message']['text'] == '/start':
                        self.BOT.send_text(Message['message']['chat']['id'],
                        'source code: \nhttps://github.com/bigAmir/Telenger/\nstart talking!',
                        0,0,Message['message']['message_id'])
### what if they were trying to spam the bot?!
                elif Message['message']['text'][0] == '/':
                        self.BOT.send_text(Message['message']['chat']['id'],
                        'DO NOT TRY TO SPAM! XD\n(messages shouldn\'t be started with "/" )',
                        0,0,Message['message']['message_id'])
### and finally, you can see the message!
                else:
                        self.BOT.send_text(Message['message']['chat']['id'],
                        'Sent! :)',
                        0,0,Message['message']['message_id'])
                        self.BOT.forward(self.BOT.ADMINID,
                        Message['message']['chat']['id'],
                        Message['message']['message_id'])

### when the bot want's to talk to you:
        def tell_admin(self, Text, ReplyToMessageID=0):
                self.BOT.send_text(self.BOT.ADMINID,Text,0,0,ReplyToMessageID)

### send your message to the user.
        def send_it(self, Message):
### if you were looking for some help:
                if Message['message']['from']['id'] == self.BOT.ADMINID and Message['message']['text'] == '/Help':
                        self.tell_admin('use /For to forward a message.',Message['message']['message_id'])
                else:
                        self.BOT.send_text(Message['message']['reply_to_message']['forward_from']['id'],
                        Message['message']['text'])
