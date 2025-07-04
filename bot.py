import requests
from models import Update
class Bot:
    def __init__(self,token :str,base_url :str):
        self.token=token
        self.base_url=base_url
    def get_update(self,update_id: int):
        url=f"{self.base_url}/getUpdates"
        params={"offset":update_id}
        r=requests.get(
            url,
            params=params
        )
        l=[]
        for update_clasi_un in r.json()["result"]:
            update=Update(update_id=update_clasi_un.get("update_id"),message=update_clasi_un.get("message"))
            l.append(update)
        return l
    def sen_message(self, chat_id :int, text :str)->dict:
        r=requests.post(
            f"{self.base_url}/sendMessage",
            params={
                "chat_id":chat_id,
                "text":f"`{text}`",
                "parse_mode":"Markdown"
            }
            )
    def send_document(self,chat_id,file_id):
        r=requests.post(
            f"{self.base_url}/sendDocument",
            data={
                "chat_id":chat_id,
                "document":file_id,
                "caption":"mana siz yuborgan file"
            }
        )
    def send_voice(self,chat_id,voice_id):
        r=requests.post(
            f"{self.base_url}/sendVoice",
            data={
                "chat_id":chat_id,
                "voice":voice_id,
                "caption":"mana siz yuborgan ovoz"
            }
        )
    def send_photo(self,chat_id,photo_id):
        r=requests.post(
            f"{self.base_url}/sendPhoto",
            data={
                "chat_id":chat_id,
                "photo":photo_id,
                "caption":"mana siz yuborgan rasm"
            }
        )
    def send_video(self,chat_id,video_id):
        r=requests.post(
            f"{self.base_url}/sendVideo",
            data={
                "chat_id":chat_id,
                "video":video_id,
                "caption":"mana siz yuborgan rasm"
            }
        )
    def send_dice(self):
        r=requests.post(
            f"{self.base_url}/sendDice",
            data={
                "chat_id":1885538461
            }
        )