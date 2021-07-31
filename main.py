colors=['yashil','qizil','sariq','oq','qora']
animals=['sichqon','sigir','yo\'lbars','quyon','ajdar','ilon','ot','qo\'y','maymun','tovuq','it','to\'ngiz']
def burch(inp_year):
	inp_year=int(inp_year)
	for i in range(1984,inp_year+1):
		x=animals[0]
		y=colors[0]
		colors.pop(0)
		animals.pop(0)
		colors.append(y)
		animals.append(x)
		if i==inp_year:
			return (str(y)+'  '+str(x)+'  '+f'--bu {inp_year} uchun')










import telebot
TOKEN='1907799671:AAHb4q3psV3g63yNEDlYKYrq03_c0tg7xKs'
bot=telebot.TeleBot(TOKEN,parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    answer="Assalomu alaykum, xush kelibsiz! "
    answer+='\nYil  kiriting: \n(masalan 2000,1997 \n1984 dan katta butun yillarni: )'
    bot.reply_to(message,answer)

@bot.message_handler(func=lambda message:True)
def echo_all(message):
	bot.reply_to(message,burch(message.text))

bot.polling()














