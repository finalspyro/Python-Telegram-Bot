import constants as keys
from telegram.ext import *
import responses as r

print("Bot started...")

def start_command(update, context):
    update.message.reply_text('Type something random to get started')

def convertc_command(update, context):
    user_input = update.message.text
    celsius = user_input.split('/convertc ')[1]
    fahrenheit = ((float(celsius) * 9)/5) + 32
    update.message.reply_text(str(fahrenheit)+'F')

def convertf_command(update, context):
    user_input = update.message.text
    fahrenheit = user_input.split('/convertf ')[1]
    celsius = ((float(fahrenheit) - 32) * 5 / 9)
    update.message.reply_text(str(celsius)+'C')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = r.sample_responses(text)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("convertc", convertc_command))
    dp.add_handler(CommandHandler("convertf", convertf_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()