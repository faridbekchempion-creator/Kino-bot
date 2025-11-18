import telebot
from telebot import types
BUT_TOKEN = "7970873160:AAGGrUzBO63pT8uiJdImnxtevOuGus7niZo"

bot = telebot.TeleBot(BUT_TOKEN)
CHENNELS=[
    "@faridbek_kinochi"
]
def check_user(user_id):
    for ch in CHENNELS:
        try:
            status = bot.get_chet_member(ch,user_id).status
            if status in ['left','kicked']:
                return False
        except:
            return False
        return True 
    
def isSubscribe(chat_id):
    markup=types.InlineKeyboardMarkup()
    for ch in CHENNELS:
        markup.add(types.InlineKeyboardButton(text=ch,url=f"https://t.me/{ch[1:]}"))

    markup.add(types.InlineKeyboardButton("TEKSHIRISH",callback_data="check"))
    bot.send_message(chat_id, "Botdan foydalanish uchun kanallarga obuna bo'lishingiz kerak!", reply_markup=markup)




@bot.callback_query_handler(func=lambda call:call.data == "check")
def check_callback(call):
    user_id = call.from_user.id
    if check_user(user_id):
        bot.send_message(call.message.chat.id,"botdan foydalanishingiz mumkin")
        bot.answer_callback_query(call.id)
    else:
        bot.send_message(call.message.chat.id,"barcha kanallarga obuna bolmagansiz\nObuna boling")
        bot.answer_callback_query(call.id)



  

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if check_user(user_id):
        bot.send_message(message.chat.id, "botdan foydalanishingiz mumkin.")
        markup=types.InlineKeyboardMarkup()
        button1=types.InlineKeyboardButton("Sonic",callback_data="Sonic")
        button2=types.InlineKeyboardButton("Uyga yol yoq", callback_data="Uyga yol yoq")
        button3=types.InlineKeyboardButton("Flesh",callback_data="Flesh")
        button4=types.InlineKeyboardButton("solo leviling", callback_data="solo leviling")
        button5=types.InlineKeyboardButton("naruto", callback_data="naruto")
        button6=types.InlineKeyboardButton("soyada kotarilish",callback_data="soyada kotarilish")
        button7=types.InlineKeyboardButton("jodugarlar jangi", callback_data="jodugarlar jangi")
        button8=types.InlineKeyboardButton("demon sleyer",callback_data="demon sleyer")
        button9=types.InlineKeyboardButton("wendnesday",callback_data="wendnesday")
        button10=types.InlineKeyboardButton("supermen",callback_data="supermen")
        markup.add(button1)
        markup.add(button2)
        markup.add(button3)
        markup.add(button4)
        markup.add(button5)
        markup.add(button6)
        markup.add(button7)
        markup.add(button8)
        markup.add(button9)
        markup.add(button10)
        bot.send_message(message.chat.id,"Film tanlang",reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Barcha kanallarga obuna bo'ling. Obuna bo'lmagansiz!")
        isSubscribe(message.chat.id)



@bot.callback_query_handler(func=lambda call:True)
def quer(call):
    if call.data == "Sonic":
        a=open("sonic.mp4","rb")
        bot.send_video(call.message.chat.id,a)
    elif call.data == "Uyga yol yoq":
        a=open("uy.mp4","rb")
        bot.send_video(call.message.chat.id,a)
    elif call.data == "Flesh":
        a=open("flash.mp4","rb")
        bot.send_video(call.message.chat.id,a)
    elif call.data == "solo leviling":
        a=open("solo.mp4","rb")
        bot.send_video(call.message.chat.id,a)
    elif call.data == "naruto":
        a=open("naruto.mp4","rb")
        bot.send_video(call.message.chat.id,a)
    elif call.data == "soyada kotarilish":
        a=open("soya","rb")
        bot.send_video(call.message.chat.id,a)
    elif call.data == "jodugarlar jangi ":=
        a=open("jj.mp4","rb")
        bot.send_video(call.message.chat.id,a)
    elif call.data == "demon sleyer":
        a=open("ds.mp4","rb")
        bot.send_video(call.message.chat.id,a)
    elif call.data == "wendnesday":
        a=open("WD.mp4","rb")
        bot.send_video(call.message.chat.id,a)
    elif call.data == "supermen":
        a=open("s.mp4","rb")
        bot.send_video(call.message.chat.id,a)
        


@bot.message_handler(func=lambda message:True)
def send(message):
    user_id = message.from_user.id
    if not check_user(user_id):
        isSubscribe(message.chat.id)
        return
    
    b = int(message.text)
    if b == 1:
        a=open("sonic.mp4","rb")
        bot.send_video(message.message.chat.id,a)
    elif b == 2:
        a=open("uy.mp4","rb")
        bot.send_video(message.message.chat.id,a)
    elif b == 3:
        a=open("flash.mp4","rb")
        bot.send_video(message.message.chat.id,a)
    elif b == 4:
        a=open("solo.mp4","rb")
        bot.send_video(message.message.chat.id,a)
    elif b == 5:
        a=open("naruto.mp4","rb")
        bot.send_video(message.message.chat.id,a)
    elif b == 6:
        a=open("soya","rb")
        bot.send_video(message.message.chat.id,a)
    elif b == 7:
        a=open("jj.mp4","rb")
        bot.send_video(message.message.chat.id,a)
    elif b == 8:
        a=open("ds.mp4","rb")
        bot.send_video(message.message.chat.id,a)
    elif b == 9:
        a=open("WD.mp4","rb")
        bot.send_video(message.message.chat.id,a)
    elif b == 10:
        a=open("s.mp4","rb")
        bot.send_video(message.message.chat.id,a)


    
print("Dastur ishga tushdi")
bot.infinity_polling() 




















