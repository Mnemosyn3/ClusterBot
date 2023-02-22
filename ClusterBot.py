import logging
from salaisuus import *
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, biip boop")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Commands:\n/start\n/ruusu  Tuska viiltää rintaa...\n/help")

async def ruusu(update: Update,context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="🌹")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="powi.fi/ruusu")
    await context.bot.send_audio(chat_id=update.effective_chat.id,audio='ruusulaulu.mp3')


if __name__ == '__main__':
    application = ApplicationBuilder().token(secret_token).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("ruusu", ruusu))

    application.run_polling()

