from pyrogram import Client
from pyrogram import filters
import random


api_id = 24777392
api_hash = "6d2aac32e13de4e457890ec3676885cc"
txt = ["лес гоу", "1", "2", "3", "4", "5", "6", "7"]

app = Client("auto_comment_sender", api_id=api_id, api_hash=api_hash)
channel = -1001353737850  #id канала
channel_chat = -1195707788 #id чата, в котором собираются комментарии канала
texted = 0


@app.on_message(filters=filters.chat([channel, channel_chat]))
async def main(client, message):
    global texted
    async for message in app.get_chat_history(chat_id=channel, limit=-1, offset_id=-1):  # Тут ид канала
        texted = message.text
        async for msg in app.get_chat_history(chat_id=channel_chat, limit=-1, offset_id=-1):  # Тут ид чата
                if msg.text == texted: 
                    texted = 0
                    await msg.reply(random.choice(txt))
                else:
                    continue

if __name__ == "__main__":
    print('[Activate]')
    app.run()