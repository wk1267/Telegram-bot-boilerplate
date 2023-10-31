from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters,ContextTypes

#global variables obtained from BotFather
TOKEN = ''
BOT_USERNAME = ''

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('hello! this is starting text')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('this is help text')

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hello!'
    else:
        return 'ok'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.message.text

    print(f'User ({update.message.chat_id} sends a text: {text}')
    response: str = handle_response(text)
    print(f'Bot: {response}')
    await update.message.reply_text(response)

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    #Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    #Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.run_polling(poll_interval=3)
