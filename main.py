import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import subprocess
import autopep8

# تعيين توكن البوت هنا
TOKEN = '6487569861:AAGt9xCKSwN_bCuLXEDVtJhjr-bAEd89HVc'
UPLOAD_FOLDER = 'uploads'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('مرحبًا! أرسل لي ملف بايثون (.py) لتصحيحه.')

def check_errors(file_path):
    """Check for errors in a Python file using flake8."""
    result = subprocess.run(['flake8', file_path], capture_output=True, text=True)
    return result.stdout

def fix_errors(file_path):
    """Fix errors in a Python file using autopep8."""
    with open(file_path, 'r') as file:
        original_code = file.read()
    
    fixed_code = autopep8.fix_code(original_code)
    
    with open(file_path, 'w') as file:
        file.write(fixed_code)
    
    return fixed_code

def handle_document(update: Update, context: CallbackContext) -> None:
    document = update.message.document
    if document.file_name.endswith('.py'):
        file = context.bot.getFile(document.file_id)
        file_path = os.path.join(UPLOAD_FOLDER, document.file_name)
        file.download(file_path)
        update.message.reply_text('تم استلام الملف، جاري الفحص والتصحيح...')
        fix_errors(file_path)
        update.message.reply_document(document=open(file_path, 'rb'), caption='تم التصحيح!')
    else:
        update.message.reply_text('الرجاء إرسال ملف بايثون بامتداد .py فقط.')

def main():
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.document, handle_document))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

