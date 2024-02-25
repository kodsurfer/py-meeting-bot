from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Замените 'YOUR_TELEGRAM_BOT_TOKEN' на токен вашего бота, полученный от BotFather в Telegram
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я помогу вам забронировать переговорную комнату.')


def book(update: Update, context: CallbackContext) -> None:
    # Здесь должна быть логика резервирования комнаты
    update.message.reply_text('Вы успешно забронировали переговорную комнату на завтра в 10:00.')


def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("book", book))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
