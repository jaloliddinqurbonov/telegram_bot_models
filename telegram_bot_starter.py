from pprint import pprint
from bot import Bot
import os
from dotenv import load_dotenv
load_dotenv()
import time

token=os.getenv("token")
base_url = f"https://api.telegram.org/bot{token}"


bot=Bot(token=token,base_url=base_url)

last_update_id = 0
while True:

    updates=bot.get_update(last_update_id)
   

    for update in updates:

       
        last_update_id = update.update_id + 1
        pprint(update.message)
        chat_id = update.message.chat.id
        
        if update.message.text:
            text=update.message.text
            bot.sen_message(chat_id=chat_id,text=text)
        elif update.message.document:
            file_id=update.message.document.get("file_id")
            bot.send_document(chat_id=chat_id,file_id=file_id)
        elif update.message.voice:
            voice_id=update.message.voice.get("file_id")
            bot.send_voice(chat_id=chat_id,voice_id=voice_id)
        elif update.message.photo:
            photo_id = update.message.photo[0].get("file_id")
            bot.send_photo(chat_id=chat_id,photo_id=photo_id)
        elif update.message.video:
            video_id = update.message.video.get("file_id")
            bot.send_video(chat_id=chat_id,video_id=video_id)
        else:
            bot.send_dice()
        time.sleep(1)
