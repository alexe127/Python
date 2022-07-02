from pickle import GLOBAL


# total_sweets = 30
# max_sweets = 10
# player = 1
# game = False


def start(update, context):
    global total_sweets, player, game, max_sweets
    total_sweets = 30
    max_sweets = 10
    player = 1
    game = True               
    context.bot.send_message(update.effective_chat.id, "Привет, начнём игру? ")
    context.bot.send_message(update.effective_chat.id, 
    "Если да введите команду /yes  для отмены  /cancel")

    
def message(update, context):
    global total_sweets, player, game      
    context.bot.send_message(update.effective_chat.id, f'На столе лежат {total_sweets} конфет')
    context.bot.send_message(update.effective_chat.id, 
    f'Сколько конфет вы берете? (не более {max_sweets}): ')
    context.bot.send_message(update.effective_chat.id, f'Ходит игрок №{player}')
    
  

def cancel(update, context):    
    context.bot.send_message(update.effective_chat.id, 
    "Очень жаль, если передумаете: запустите игру командой /start")
    

def couse_game(update, context):
    global total_sweets, player, game 
    text = update.message.text    
    if not game:
        context.bot.send_message(update.effective_chat.id, f'Запустите игру командой /start ')
        return
    if not text.isdigit() or int(text) == 0:
        context.bot.send_message(update.effective_chat.id, f'Введите правильное значение.') 
    elif int(text) > max_sweets:
        context.bot.send_message(update.effective_chat.id, f'Вы ввели значение больше {max_sweets}, будьте внимательней!')
    elif total_sweets <= max_sweets and int(text) > total_sweets:
        context.bot.send_message(update.effective_chat.id, 
        f'Вы ввели значение больше чем конфет на столе, будьте внимательней!')
    else:
        take_candies = int(text)
        total_sweets = total_sweets - take_candies
        context.bot.send_message(update.effective_chat.id, f'Осталось {total_sweets} конфет')
        if total_sweets == 1:
            context.bot.send_message(update.effective_chat.id, f'Выиграл игрок №{player}')
            context.bot.send_message(update.effective_chat.id, 
            f'для продолжения введите команду /start,  для выхода  /cancel ')                          
            return
        player = 2 if player == 1 else 1
        context.bot.send_message(update.effective_chat.id, f'Ходит игрок №{player}')
        if total_sweets == 0:
            context.bot.send_message(update.effective_chat.id, f'Выиграл игрок №{player}')
            context.bot.send_message(update.effective_chat.id, 
            f'для продолжения введите команду /start,  для выхода  /cancel ')           
            return