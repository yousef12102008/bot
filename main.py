import requests
import telebot
import asyncio
from telebot import types
from mk import Tele
import os

token = '6848019028:AAGDVZ4MIlMKOL0pRjtjMOadz4qkf9cqarU'
bot = telebot.TeleBot(token, parse_mode="HTML")

# قائمة ID المسموح لهم
allowed_ids = [6309252183]

@bot.message_handler(commands=["start"])
def start(message):
    if message.chat.id not in allowed_ids:
        bot.reply_to(message, "🚫 You cannot use the bot. Contact developers to purchase a bot subscription @Af5AA")
        return
    bot.reply_to(message, "📂 Send the file now \n 📨 ارسل الملف الان")

@bot.message_handler(commands=["stop"])
def stop(message):
    if message.chat.id in allowed_ids:
        with open("stop.stop", "w") as file:
            pass
        bot.reply_to(message, "🛑 The bot has been stopped. ✅")

@bot.message_handler(content_types=["document"])
def handle_document(message):
    if message.chat.id not in allowed_ids:
        bot.reply_to(message, "🚫 You cannot use the bot. Contact developers to purchase a bot subscription @Af5AA")
        return
    asyncio.run(main(message))

async def main(message):
    live = 0
    declined = 0
    ko = bot.reply_to(message, "⌛ Checking Your Cards...").message_id
    ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
    with open("combo.txt", "wb") as w:
        w.write(ee)

    try:
        with open("combo.txt", 'r') as file:
            lino = file.readlines()
            total = len(lino)
            if total > 2000000:
                bot.reply_to(message, "🚫 You have exceeded the limit of 2000 cards. You will be banned.")
                return
            for cc in lino:
                if os.path.exists("stop.stop"):
                    bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='🛑 STOPPED ✅\nBOT BY ➜ @Af5AA')
                    os.remove('stop.stop')
                    return
                
                try:
                    data = requests.get('https://lookup.binlist.net/' + cc[:6]).json()
                except:
                    data = {}
                
                bank = data.get('bank', {}).get('name', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                emj = data.get('country', {}).get('emoji', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                cn = data.get('country', {}).get('name', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                dicr = data.get('scheme', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                typ = data.get('type', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                url = data.get('bank', {}).get('url', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')

                try:
                    last = str(Tele(cc))
                except Exception as e:
                    print(e)
                    last = "ERROR"

                if 'risk' in last:
                    last = 'declined'
                elif 'Duplicate' in last:
                    last = 'Approved'

                mes = types.InlineKeyboardMarkup(row_width=1)
                cm1 = types.InlineKeyboardButton(f"💳 {cc} 💳", callback_data='u8')
                status = types.InlineKeyboardButton(f"📊 STATUS ➜ {last}", callback_data='u8')
                cm3 = types.InlineKeyboardButton(f"✅ APPROVED ➜ [ {live} ]", callback_data='x')
                cm4 = types.InlineKeyboardButton(f"❌ DECLINED ➜ [ {declined} ]", callback_data='x')
                cm5 = types.InlineKeyboardButton(f"📊 TOTAL ➜ [ {total} ]", callback_data='x')
                stop = types.InlineKeyboardButton(f"🛑 [ STOP ]", callback_data='stop')
                mes.add(cm1, status, cm3, cm4, cm5, stop)

                bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='🔄 Wait for processing by @Af5AA', reply_markup=mes)

                msg = f'''◆ CARD ➜ {cc} 
◆ STATUS ➜ APPROVED 🔥
◆ RESULT ➜ #Approved
◆ GATEWAY ➜ BRAINTREE AUTH 
━━━━━━━━━━━━━━━━━
◆ BIN ➜ {cc[:6]} - {dicr} - {typ} 
◆ COUNTRY ➜ {cn} - {emj} 
◆ BANK ➜ {bank}
◆ URL ➜ {url}
━━━━━━━━━━━━━━━━━
◆ BY: @Af5AA
'''
                print(last)

                if "live" in last or 'Approved' in last:
                    live += 1
                    bot.reply_to(message, msg)
                else:
                    declined += 1
                
                await asyncio.sleep(21)
    except Exception as e:
        print(e)
    bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='✔️ COMPLETED ✅\nBOT BY ➜ @Af5AA')

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
    with open("stop.stop", "w") as file:
        pass

print("تم تشغيل البوت")
bot.polling()
