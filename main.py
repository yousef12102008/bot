import os
import random
import re
import requests
from telegram import Update, InputFile, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler

# وظيفة للحصول على معلومات البطاقة باستخدام API
def info(card):
    while True:
        response = requests.get('https://bins.antipublic.cc/bins/' + card[:6])
        
        if 'not found' in response.text:
            return ("------", "------", "------", "------", "------", "------")
        elif 'Cloudflare' in response.text:
            break
        elif response.status_code == 200:
            break

    if response.status_code == 200:
        data = ['brand', 'type', 'level', 'bank', 'country_name', 'country_flag']
        result = []
        
        for field in data:
            try:
                result.append(response.json().get(field, "------"))
            except:
                result.append("------")  
    
        return tuple(result)
    else:
        return ("------", "------", "------", "------", "------", "------")

# وظائف لقراءة وكتابة الفيزا
def read_visas(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        visas = file.readlines()
    return [visa.strip() for visa in visas]

def write_visas(file_path, visas):
    with open(file_path, 'w', encoding='utf-8') as file:
        for visa in visas:
            file.write(visa + '\n')

# وظائف لتنظيف وخلط وتصحيح الفيزا
def clean_visas(visas):
    cleaned_visas = [visa.replace(' ', '') for visa in visas if visa.strip()]
    return cleaned_visas

def shuffle_visas(visas):
    random.shuffle(visas)
    return visas

def fix_visas(visas):
    fixed_visas = []
    for visa in visas:
        visa = re.sub(r'\D', '', visa)
        if len(visa) in {13, 16}:
            fixed_visas.append(visa)
    return fixed_visas

# وظيفة لفلترة الفيزا بناءً على BIN والدولة والبنك
def filter_visas(visas, bin=None, country=None, bank=None):
    filtered_visas = []
    for visa in visas:
        card_info = info(visa)
        if (bin is None or visa.startswith(bin)) and \
           (country is None or card_info[4].strip().upper() == country.strip().upper()) and \
           (bank is None or card_info[3].strip().upper() == bank.strip().upper()):
            filtered_visas.append(visa)
    return filtered_visas

# وظائف الأوامر
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("تنظيف", callback_data='clean'), InlineKeyboardButton("خلط", callback_data='shuffle')],
        [InlineKeyboardButton("تصحيح", callback_data='fix')],
        [InlineKeyboardButton("تحديد BIN", callback_data='set_bin')],
        [InlineKeyboardButton("تحديد الدولة", callback_data='set_country')],
        [InlineKeyboardButton("تحديد البنك", callback_data='set_bank')],
        [InlineKeyboardButton("التحقق من BIN", callback_data='check_bin')],
        [InlineKeyboardButton("حذف عدد من الفيز", callback_data='remove')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('أهلاً! اختر العملية اللي عايز تعملها:', reply_markup=reply_markup)

def handle_file(update: Update, context: CallbackContext) -> None:
    file = update.message.document.get_file()
    file_path = 'input_visas.txt'
    file.download(file_path)

    bin = context.user_data.get('bin')
    country = context.user_data.get('country')
    bank = context.user_data.get('bank')

    visas = read_visas(file_path)
    context.user_data['visas'] = visas

    filtered_visas = filter_visas(visas, bin, country, bank)

    shuffled_visas = shuffle_visas(filtered_visas)
    
    output_file_path = 'shuffled_visas.txt'
    write_visas(output_file_path, shuffled_visas)

    with open(output_file_path, 'rb') as output_file:
        update.message.reply_document(document=InputFile(output_file), filename='shuffled_visas.txt')

    os.remove(file_path)
    os.remove(output_file_path)

def clean_command(update: Update, context: CallbackContext) -> None:
    visas = context.user_data.get('visas', [])
    if not visas:
        update.message.reply_text('لم يتم العثور على فيز لتنظيفها. الرجاء إرسال ملف فيز أولاً.')
        return

    cleaned_visas = clean_visas(visas)
    output_file_path = 'cleaned_visas.txt'
    write_visas(output_file_path, cleaned_visas)

    with open(output_file_path, 'rb') as output_file:
        update.message.reply_document(document=InputFile(output_file), filename='cleaned_visas.txt')

    os.remove(output_file_path)

def shuffle_command(update: Update, context: CallbackContext) -> None:
    visas = context.user_data.get('visas', [])
    if not visas:
        update.message.reply_text('لم يتم العثور على فيز لخلطها. الرجاء إرسال ملف فيز أولاً.')
        return

    shuffled_visas = shuffle_visas(visas)
    output_file_path = 'shuffled_visas.txt'
    write_visas(output_file_path, shuffled_visas)

    with open(output_file_path, 'rb') as output_file:
        update.message.reply_document(document=InputFile(output_file), filename='shuffled_visas.txt')

    os.remove(output_file_path)

def fix_command(update: Update, context: CallbackContext) -> None:
    visas = context.user_data.get('visas', [])
    if not visas:
        update.message.reply_text('لم يتم العثور على فيز لتصحيحها. الرجاء إرسال ملف فيز أولاً.')
        return

    fixed_visas = fix_visas(visas)
    output_file_path = 'fixed_visas.txt'
    write_visas(output_file_path, fixed_visas)

    with open(output_file_path, 'rb') as output_file:
        update.message.reply_document(document=InputFile(output_file), filename='fixed_visas.txt')

    os.remove(output_file_path)

def remove_command(update: Update, context: CallbackContext) -> None:
    try:
        number_to_remove = int(context.args[0].strip())
        visas = context.user_data.get('visas', [])
        if not visas:
            update.message.reply_text('لم يتم العثور على فيز. الرجاء إرسال ملف فيز أولاً.')
            return

        if number_to_remove > len(visas):
            update.message.reply_text(f'العدد المطلوب أكبر من عدد الفيز المتاحة. العدد المتاح هو {len(visas)}.')
            return

        remaining_visas = visas[number_to_remove:]
        context.user_data['visas'] = remaining_visas

        output_file_path = 'remaining_visas.txt'
        write_visas(output_file_path, remaining_visas)

        with open(output_file_path, 'rb') as output_file:
            update.message.reply_document(document=InputFile(output_file), filename='remaining_visas.txt')

        os.remove(output_file_path)
    except (IndexError, ValueError):
        update.message.reply_text('يرجى استخدام الأمر /remove متبوعًا بعدد صحيح. مثال: /remove 5')

def set_bin(update: Update, context: CallbackContext) -> None:
    try:
        bin = context.args[0].strip()
        context.user_data['bin'] = bin
        update.message.reply_text(f'BIN {bin} تم استلامه.')
    except IndexError:
        update.message.reply_text('يرجى استخدام الأمر /bin متبوعًا بـ BIN. مثال: /bin 521403')

def set_country(update: Update, context: CallbackContext) -> None:
    try:
        country = ' '.join(context.args).strip().upper()
        context.user_data['country'] = country
        update.message.reply_text(f'اسم الدولة {country} تم استلامه.')
    except IndexError:
        update.message.reply_text('يرجى استخدام الأمر /country متبوعًا باسم الدولة. مثال: /country UNITED STATES')

def set_bank(update: Update, context: CallbackContext) -> None:
    try:
        bank = ' '.join(context.args).strip().upper()
        context.user_data['bank'] = bank
        update.message.reply_text(f'اسم البنك {bank} تم استلامه.')
    except IndexError:
        update.message.reply_text('يرجى استخدام الأمر /bank متبوعًا باسم البنك. مثال: /bank CHASE')

def check_bin(update: Update, context: CallbackContext) -> None:
    try:
        bin = context.args[0].strip()
        card_info = info(bin + "0000000000")
        response_message = (f"BIN: {bin}\n"
                            f"Brand: {card_info[0]}\n"
                            f"Type: {card_info[1]}\n"
                            f"Level: {card_info[2]}\n"
                            f"Bank: {card_info[3]}\n"
                            f"Country: {card_info[4]}\n"
                            f"Country Flag: {card_info[5]}")
        update.message.reply_text(response_message)
    except IndexError:
        update.message.reply_text('يرجى استخدام الأمر /checkbin متبوعًا بـ BIN. مثال: /checkbin 521403')

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    command = query.data
    if command == 'clean':
        clean_command(query, context)
    elif command == 'shuffle':
        shuffle_command(query, context)
    elif command == 'fix':
        fix_command(query, context)
    elif command == 'set_bin':
        query.message.reply_text('يرجى إرسال BIN باستخدام الأمر /bin <BIN>.')
    elif command == 'set_country':
        query.message.reply_text('يرجى إرسال اسم الدولة باستخدام الأمر /country <COUNTRY>.')
    elif command == 'set_bank':
        query.message.reply_text('يرجى إرسال اسم البنك باستخدام الأمر /bank <BANK>.')
    elif command == 'check_bin':
        query.message.reply_text('يرجى إرسال BIN للتحقق باستخدام الأمر /checkbin <BIN>.')
    elif command == 'remove':
        query.message.reply_text('يرجى إرسال عدد الفيز المطلوب حذفها باستخدام الأمر /remove <عدد>.')

def main() -> None:
    TOKEN = '7395612598:AAGS5vDEW1i65Dnp9VfqPLDsR1Mn79E7H0o'

    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("bin", set_bin))
    dispatcher.add_handler(CommandHandler("country", set_country))
    dispatcher.add_handler(CommandHandler("bank", set_bank))
    dispatcher.add_handler(CommandHandler("checkbin", check_bin))
    dispatcher.add_handler(CommandHandler("remove", remove_command))
    dispatcher.add_handler(MessageHandler(Filters.document.mime_type("text/plain"), handle_file))
    dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
