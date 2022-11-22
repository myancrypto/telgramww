import os
import telebot

chat_id = 12345

button_1 = telebot.types.InlineKeyboardButton('1.NFT ဘယ်လို ကိုယ်တိုင်လုပ်မလဲ', callback_data='b1')
button_2 = telebot.types.InlineKeyboardButton('2.NFT ကိုယ်တိုင် ဘယ်လိုလုပ်မလဲ', callback_data='b2')
button_3 = telebot.types.InlineKeyboardButton('3.Discord တွေမှာ NFT တွေနဲ့ ဘယ်လို ပိုက်ဆံ ရှာကြတာလဲ', callback_data='b3')
button_4 = telebot.types.InlineKeyboardButton('4.Sunday talkie podcast 002', callback_data='b4')
button_5 = telebot.types.InlineKeyboardButton('5.Sunday talkie podcast 003', callback_data='b5')
button_6 = telebot.types.InlineKeyboardButton('6.Sunday talkie podcast 004', callback_data='b6')
button_7 = telebot.types.InlineKeyboardButton('7.Sunday talkie podcast 005', callback_data='b7')
button_8 = telebot.types.InlineKeyboardButton('8.Sunday talkie podcast 007', callback_data='b8')
button_9 = telebot.types.InlineKeyboardButton('9.Facebook Profile မှာ NFT တင်နည်း', callback_data='b9')
button_10 = telebot.types.InlineKeyboardButton('10.Facebook page မှာ NFT တင်နည်း', callback_data='b10')
button_11 = telebot.types.InlineKeyboardButton('11.Instagram မှာ NFT တင်နည်း', callback_data='b11')


keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.add(button_1)
keyboard.add(button_2)
keyboard.add(button_3)
keyboard.add(button_4)
keyboard.add(button_5)
keyboard.add(button_6)
keyboard.add(button_7)
keyboard.add(button_8)
keyboard.add(button_9)
keyboard.add(button_10)
keyboard.add(button_11)



API_KEY = "5731101707:AAGTvcxGSvqgeFvEKMejGG8F-Y3-bp29Pbc"
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Myan Crypto Community မှ ကြိုဆိုလိုက်ပါတယ် NFT သင်ခန်းစာများကို လေ့လာလိုပါက ဖော်ပြထားသော button ကို နှိပ်ပါ", reply_markup=keyboard)
	


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "b1":
      bot.send_message(call.message.chat.id,"https://youtu.be/1N4mL4Q9kq8")
    elif call.data == "b2":
        bot.send_message(call.message.chat.id,"https://youtu.be/Xy3lhhr8KEM")
    elif call.data == "b3":
        bot.send_message(call.message.chat.id,"https://youtu.be/i3NkMTWs4NQ")
    elif call.data == "b4":
        bot.send_message(call.message.chat.id,"https://youtu.be/Kd9RX1wjmIc")
    elif call.data == "b5":
        bot.send_message(call.message.chat.id,"https://youtu.be/AOsngbmlNTs")
    elif call.data == "b6":
        bot.send_message(call.message.chat.id,"https://youtu.be/3djHmaOuybw")
    elif call.data == "b7":
        bot.send_message(call.message.chat.id,"https://youtu.be/MXYXam_qEGs")
    elif call.data == "b8":
        bot.send_message(call.message.chat.id,"https://youtu.be/7IrdHfz_2kM")
    elif call.data == "b9":
        bot.send_message(call.message.chat.id,"https://m.facebook.com/story.php?story_fbid=pfbid0kkL2j3yLCyHp17b7kZduGtuvXYzCKzAzrRfEzoJBH2JEJVzGzpDSh4KKtj67M54pl&id=102378605298175&eav=AfYV6qltm4LjUm-MPHN-ejnJWxbLqKaAK4UpY-i_K90W2NmL5_4QX7lJgHSCfj0Qs6I&refid=52&__tn__=%2As-R&paipv=0")
    elif call.data == "b10":
        bot.send_message(call.message.chat.id,"https://m.facebook.com/story.php?story_fbid=pfbid02T8n1wJvQeaLDSjYZowQgFWmadmBDu6Jah6fzA6mpF7YNiQ3Tpwtugvn1hkG1vyaYl&id=102378605298175&eav=AfZBCf2H6oqaAlLCZR__8Diw0_PCdRVKOeW_yA8-KTg5Dl7x-HQhvDtIKF2JLdtlXTI&refid=52&__tn__=%2As-R&paipv=0")
    elif call.data == "b11":
        bot.send_message(call.message.chat.id,"https://m.facebook.com/story.php?story_fbid=pfbid02JCTy9Sx2c1asFQRqFwexic6WDPJJ3ViPH4kJFwcW2C9bvR1xBhYWcXf792LzKhtHl&id=102378605298175&eav=AfbYQALSosrQNqXq9HQEOtWWUEEcROa2wMowVy98UEC6uiLYagEuRI-wEZg07E5-rgo&refid=52&__tn__=%2As-R&paipv=0")    



bot.polling()