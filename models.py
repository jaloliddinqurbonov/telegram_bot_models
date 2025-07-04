class Update:
    def __init__(self,update_id :int,message :str):
        self.update_id=update_id
        self.message=Message(
            message_id=message["message_id"],
            from_user=message["from"],
            chat=Chat(
                id=message["chat"]["id"],
                first_name=message["chat"]["first_name"],
                username=message["chat"]["username"]  
            ),
            date=message["date"],
            text=message.get("text"),
            voice=message.get("voice"),
            document=message.get("document"),   
            photo=message.get("photo"),
            video=message.get("video")
        )

class Message:
    def __init__(self,message_id :int,from_user,chat,date:int,text:str,voice,document,photo,video):
        self.message_id=message_id
        self.from_user=from_user
        self.chat=chat
        self.date=date
        self.text=text  
        self.voice=voice
        self.document=document
        self.photo=photo
        self.video=video

class Chat:
    def __init__(self,id,first_name,username):
        self.id=id
        self.first_name=first_name
        self.username=username