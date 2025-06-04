from bot import TelegramBot
import time

# Main bot loop
def main():
    # Replace with your bot token from @BotFather
    BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
    bot = TelegramBot(BOT_TOKEN)
    
    print("Bot started. Send messages to test...")
    
    while True:
        updates = bot.get_updates()
        
        for update in updates:
            if update.message:
                print(f"Received: {update}")
                
                # Echo back a response for text messages
                if update.message.text:
                    bot.send_message(
                        update.message.chat.id, 
                        f"You said: {update.message.text}"
                    )
                
                # TODO: Students will add handling for voice, photo, and dice messages here
                # For example:
                # if update.message.voice:
                #     print(f"Voice message received: {update.message.voice}")
                # if update.message.photo:
                #     print(f"Photo message received: {update.message.photo}")
                # if update.message.dice:
                #     print(f"Dice rolled: {update.message.dice}")
        
        time.sleep(1)

if __name__ == "__main__":
    main()
