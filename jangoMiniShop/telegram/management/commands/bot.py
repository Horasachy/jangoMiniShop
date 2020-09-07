import telebot
from telebot import types
from django.core.management.base import BaseCommand
from jangoMiniShop import settings
from products.models import Product
import os

bot = telebot.TeleBot(settings.TELEGRAM_API_TOKEN)


class Command(BaseCommand):
    help = 'Telegram Bot'

    def handle(self, *args, **options):
        @bot.message_handler(content_types=['text'])
        def any_message(message):
            Keyboard = types.InlineKeyboardMarkup(row_width=2)
            first_button = types.InlineKeyboardButton(text='products', callback_data='products')
            Keyboard.add(first_button)
            bot.send_message(message.chat.id, 'test', reply_markup=Keyboard)

        @bot.callback_query_handler(func=lambda call: call.data == 'main')
        def callback_inline(call):
            Keyboard = types.InlineKeyboardMarkup(row_width=2)
            first_button = types.InlineKeyboardButton(text="products", callback_data="products")
            Keyboard.add(first_button)
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text="menu",
                                  reply_markup=Keyboard)

        @bot.callback_query_handler(func=lambda call: call.data == 'products')
        def callback_inline(call):
            Keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="1", callback_data="1")
            btn2 = types.InlineKeyboardButton(text="2", callback_data="2")
            btn3 = types.InlineKeyboardButton(text="3", callback_data="3")
            back_btn = types.InlineKeyboardButton(text="back", callback_data="main")
            Keyboard.add(btn1, btn2, btn3, back_btn)
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text="replaced text",
                                  reply_markup=Keyboard)

        @bot.message_handler(commands=['products'])
        def get_products(message):
            working_directory = os.getcwd()
            products = Product.objects.all()
            for product in products:
                bot.send_photo(
                    message.chat.id,
                    open(working_directory + settings.MEDIA_URL + product.preview_image.name, 'rb'),
                    caption="Product name: " + product.name
                )
                bot.send_message(message.chat.id, message.from_user.username)

        @bot.message_handler(commands=['order'])
        def create_order(message):
            pass

        bot.polling(none_stop=True)
