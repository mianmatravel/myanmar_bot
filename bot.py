from telegram import Update
from telegram.ext import Application, CommandHandler

TOKEN = "8669898485:AAHSfPIZnsWn3_OWFLqavUxX1IOQfKlxX1w"

async def start(update, context):
    await update.message.reply_text("机器人已启动！发送 /usd 查美元，/cny 查人民币")

async def usd(update, context):
    await update.message.reply_text("1 美元 = 3500 缅币")

async def cny(update, context):
    await update.message.reply_text("1 人民币 = 485 缅币")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("usd", usd))
    app.add_handler(CommandHandler("cny", cny))
    print("机器人运行中...")
    app.run_polling()

if __name__ == "__main__":
    main()