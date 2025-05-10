from telegram.ext import Updater, CommandHandler

TOKEN = "267075:babf48ab-fea6-4d00-8bfa-6f5d1b154e57"
CHANNEL_LINK = "https://eitaa.com/karimeahle_beit"

def start(update, context):
    message = f"سلام! برای عضویت در کانال، روی لینک زیر کلیک کن:
{CHANNEL_LINK}"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
