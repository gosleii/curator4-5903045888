import telebot
from telebot import types

bot = telebot.TeleBot('7419515548:AAGfhCvFHEUmSxBA0-dbQueodduewVqFXvU')
got_name = ''


@bot.message_handler(commands=['start'])
def strt(message):
    bot.send_message(message.chat.id, 'Приветствую, мечтатель!')


@bot.message_handler(commands=['poem'])
def pm(message):
    bot.send_message(message.chat.id, '*Обязательства*                                                                                            \
Я не знаю других обязательств,                                                                               \
Кроме девственной веры в себя.                                                                               \
Этой истине нет доказательств,                                                                               \
Эту тайну я понял, любя.                                                                                     \
Бесконечны пути совершенства,                                                                                \
О, храни каждый миг бытия!                                                                                   \
В этом мире одно есть блаженство -                                                                           \
Сознавать, что ты выше себя.                                                                                 \
Презренье - бесстрастие - нежность -                                                                         \
Эти три - вот дорога твоя.                                                                                   \
Хорошо, уносясь в безбрежность,                                                                              \
За собою видеть себя.                                                                                        \
*Автор: В. Я. Брюсов*', parse_mode='Markdown')


@bot.message_handler(commands=['link'])
def lnk(message):
    bot.send_message(message.chat.id,
                     '[Ссылка на расслабляющий сайт. Во время просмотра подумайте, что значит для вас слово "совершенство".](https://www.airtightinteractive.com/demos/ribbons/)',
                     parse_mode='Markdown')


@bot.message_handler(commands=['name'])
def nm(message):
    bot.send_message(message.chat.id, 'Придумай мне имя, о котором будем знать только мы)')
    bot.register_next_step_handler(message, get_name)


def get_name(message):
    global got_name
    got_name = message.text
    if got_name != '' and 0 < len(got_name) <= 20 and got_name.find('bot') != -1 and got_name[0].isalpha():
        bot.send_message(message.chat.id, 'Прекрасно')
    else:
        bot.send_message(message.chat.id, 'Мне не нравится')


@bot.message_handler(commands=['survey'])
def srv(message):
    markup = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton('Искусство', callback_data='1')
    b2 = types.InlineKeyboardButton('Грёзы', callback_data='2')
    b3 = types.InlineKeyboardButton('Вселенная', callback_data='3')
    b4 = types.InlineKeyboardButton('Ничего', callback_data='4')
    for i in (b1, b2, b3, b4):
        markup.row(i)
    bot.send_message(message.chat.id, 'Что для вас является идеальным?', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callbckquery(callback):
    if callback.data == '1':
        bot.send_message(callback.message.chat.id,
                         'В этом есть доля правды. Искусство воспринимается и интерпретируется субъективно, и то, что один человек считает идеальным, другой может найти несовершенным.')
    if callback.data == '2':
        bot.send_message(callback.message.chat.id, 'Люди вольны предаваться фантазиям. Они могут быть _совершенными_',
                         parse_mode='Markdown')
    if callback.data == '3':
        bot.send_message(callback.message.chat.id,
                         'Вселенная является сложной и изменчивой системой, в которой существует множество несовершенств и хаоса, разнообразия и гармонии.')
    if callback.data == '4':
        bot.send_message(callback.message.chat.id,
                         'Хотя в этом мире есть много прекрасных, вдохновляющих и значимых вещей, ничто не может быть названо идеальным в абсолютном смысле.')


@bot.message_handler(content_types=['text'])
def txt(message):
    if message.text:
        bot.send_message(message.from_user.id, 'Прошу прощения, я понимаю только команды из меню')


bot.infinity_polling()

