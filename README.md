# Instructions for Copilot: Creating Student Homework for Telegram Bot API OOP

## Context

You (Copilot) are to create a homework assignment for students who are learning the Telegram Bot API and OOP in Python. The students are provided with the following object classes: `User`, `Chat`, `Message`, and `Update`. They are **NOT** given implementations for the `Voice`, `Photo`, and `Dice` classes. The students are expected to implement these themselves.

## Homework Goals

- Practice OOP by parsing complex, nested JSON structures from Telegram updates.
- Understand how to extend and integrate new data types with existing code.
- Work with the Telegram Bot API using Python and requests.

## Instructions to Copilot

1. **Present the given starter code** which includes the `User`, `Chat`, `Message`, and `Update` classes, as well as the main bot loop that uses these classes.
2. **Clearly state the student tasks:**
    - Implement the `Voice`, `Photo`, and `Dice` classes according to the Telegram Bot API documentation.
    - Modify the `Message` class to parse these new objects if their data appears in an incoming message.
    - Test their implementation by sending different types of messages (voice, photo, dice) to the bot and printing/logging the resulting objects.
3. **Provide helpful hints:**
    - Suggest which fields to parse for each class (for example, `file_id`, `duration` for `Voice`).
    - For `Photo`, explain that it is a list of sizes and may need a list of objects or a simple representation.
    - For `Dice`, mention the relevant fields as per the Telegram API.
4. **Optional Extensions:** Encourage students to add `__str__` or `__repr__` methods for easier debugging and logging.
5. **Sample structure:**
    - Starter code block
    - Task list
    - Hints and API reference links
    - Example output or testing snippet

## Example Output

Copilot should generate a Markdown homework file that includes:

- The given starter code
- A clear list of tasks for students
- Hints for each new class
- Links to [Telegram Bot API documentation](https://core.telegram.org/bots/api#message)
- Encouragement to test by sending different message types and printing the resulting Python objects

---
**End of Instructions**

