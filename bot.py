
import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("8086953920:AAGYBOwM4ysQ0bZKrOJn0IADQE439nz1t2E")
UPLOADER_URL = os.getenv("UPLOADER_URL")

async def handle_txt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = update.message.document
    if not file.file_name.endswith('.txt'):
        await update.message.reply_text("Please send a .txt file only.")
        return

    file_obj = await file.get_file()
    file_bytes = await file_obj.download_as_bytearray()
    files = {'file': (file.file_name, file_bytes)}
    
    response = requests.post(UPLOADER_URL, files=files)
    if response.ok:
        data = response.json()
        await update.message.reply_text(
            f"Uploaded '{data['filename']}' successfully.\nContent:\n{data['content'][:1000]}"
        )
    else:
        await update.message.reply_text("Upload failed.")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.Document.FILE, handle_txt))
app.run_polling()
