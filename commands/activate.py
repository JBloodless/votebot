import command_system

def hello():
   message = 'Наши милые участницы: \n\nВаля Чурилина - «О печенюшках»\n\nКарина Чилова - Stand Up «Про школу, баскетбол и феминизм»\n\nМарина Полянская - «I’ll never leave you (for better or for worse)»\n\nКатя Кофанова - монолог «О себе»\n\nУльяна Монахова - танец «Чувства»\n\nВиолетта Палий - песня «Этажи»\n\nНастя Коробкина - Stand Up «Про Настю, вещи и футбол»\n\nНаташа Жаринова - «Светошоу Наташи, комнаты и лампы»\n\nЛера Лебедева - «Ботай»\n\nНаташа Успенская - танец «This is me»'
   buttons = open("/home/votebot/mysite/defaultKeys.json", "r", encoding="UTF-8").read()
   return message, '', buttons

#hello_command = command_system.Command()

#hello_command.keys = ['Голосовать', 'Голосовать!', 'vote', 'Голосование']
#hello_command.description = 'активация'
#hello_command.process = hello
