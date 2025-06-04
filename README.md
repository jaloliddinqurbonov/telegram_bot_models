# Telegram Bot API OOP Homework

## Project Overview

This homework assignment teaches Object-Oriented Programming (OOP) concepts through building a Telegram Echo Bot. Students will work with the Telegram Bot API to create a bot that can receive and echo back different types of media messages including text, voice, photos, videos, and dice.

## Learning Objectives

- Practice OOP by parsing complex, nested JSON structures from Telegram updates
- Understand how to extend and integrate new data types with existing code
- Work with the Telegram Bot API using Python and requests
- Build a functional echo bot that handles multiple media types
- Learn proper code organization and module separation

## Project Structure

The workspace is organized into separate modules for better code organization:

```
telegram_bot_models/
├── models.py              # Data model classes (User, Chat, Message, Update)
├── bot.py                 # TelegramBot API client class
├── main.py               # Main bot loop (students create this)
├── requirements.txt      # Project dependencies
├── telegram_bot_starter.py  # Alternative single-file starter
└── README.md            # This file
```

## Student Tasks

### Phase 1: Implement Missing Model Classes (models.py)

Students need to implement three missing classes in `models.py`:

1. **Voice Class** - Parse voice message data
   - Required fields: `file_id`, `file_unique_id`, `duration`
   - Optional fields: `mime_type`, `file_size`

2. **Photo Class** - Parse photo data (array of different sizes)
   - Required fields per size: `file_id`, `file_unique_id`, `width`, `height`
   - Optional fields: `file_size`
   - Note: Photos come as arrays of different sizes

3. **Dice Class** - Parse dice roll data
   - Required fields: `emoji`, `value`

4. **Video Class** - Parse video message data
   - Required fields: `file_id`, `file_unique_id`, `width`, `height`, `duration`
   - Optional fields: `mime_type`, `file_size`

### Phase 2: Update Message Class (models.py)

Modify the `Message` class constructor to parse new object types:
- Add parsing for `voice`, `photo`, `dice`, and `video` from message data
- Initialize these attributes as `None` when not present

### Phase 3: Implement Echo Bot Methods (bot.py)

Complete the echo bot methods in `bot.py`:

1. **send_dice()** - Send animated dice back to user
2. **send_voice()** - Echo voice messages using file_id
3. **send_photo()** - Echo photos using file_id with optional caption
4. **send_video()** - Echo videos using file_id with optional caption
5. **echo_message()** - Main method that determines message type and echoes appropriately

### Phase 4: Create Main Bot Loop (main.py)

Create `main.py` with:
- Bot initialization with token
- Main loop using `get_updates()`
- Call `echo_message()` for each received message
- Proper error handling and logging

## Getting Started

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Get a bot token:**
   - Message [@BotFather](https://t.me/botfather) on Telegram
   - Create a new bot with `/newbot`
   - Save the token provided

3. **Choose your starting approach:**
   - **Modular approach:** Work with separate `models.py`, `bot.py`, and create `main.py`
   - **Single file approach:** Use `telegram_bot_starter.py` as a starting point

4. **Test your implementation:**
   - Run your bot
   - Send different message types (text, voice, photo, dice, video)
   - Verify that messages are echoed back correctly

## API Documentation

For detailed information about Telegram Bot API objects:

- [Message Object](https://core.telegram.org/bots/api#message)
- [Voice Object](https://core.telegram.org/bots/api#voice)
- [PhotoSize Object](https://core.telegram.org/bots/api#photosize)
- [Dice Object](https://core.telegram.org/bots/api#dice)
- [Video Object](https://core.telegram.org/bots/api#video)

## Example Bot Behavior

When fully implemented, your bot should:

1. **Text messages:** Echo back the exact text
2. **Voice messages:** Send back the same voice file
3. **Photos:** Send back the same photo (optionally with a caption)
4. **Videos:** Send back the same video (optionally with a caption)
5. **Dice:** Send back a dice roll with the same emoji

## Common Challenges

- **Photo handling:** Remember photos come as arrays of different sizes
- **File IDs:** Use `file_id` from received media to echo it back
- **Message parsing:** Check for `None` values when accessing message attributes
- **Error handling:** Implement proper try-catch blocks for API calls

## Submission Requirements

Your completed project should include:

1. **models.py** - Complete implementations of Voice, Photo, Dice, and Video classes
2. **bot.py** - Implemented echo methods (send_dice, send_voice, send_photo, send_video, echo_message)
3. **main.py** - Working main loop that demonstrates all functionality
4. **Testing evidence** - Screenshots or logs showing successful echoing of different message types

## Tips for Success

- Test each phase incrementally - don't try to implement everything at once
- Use `print()` statements to debug JSON structures from Telegram
- Read the Telegram Bot API documentation carefully
- Start with the simplest classes (Dice) before moving to more complex ones (Photo)
- Use the `__str__` methods for easier debugging

