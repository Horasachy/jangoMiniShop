import telebot
import os
from django.core.paginator import Paginator
from telebot import types
from telegram_bot_pagination import InlineKeyboardPaginator
from django.core.management.base import BaseCommand
from jangoMiniShop import settings
from products.models import Product
from telegram.models import TelegramOrder

bot = telebot.TeleBot(settings.TELEGRAM_API_TOKEN)
working_directory = os.getcwd()

orders = TelegramOrder.objects.all()


class Command(BaseCommand):
    help = 'Telegram Bot'

    def handle(self, *args, **options):
        @bot.message_handler(commands=['start'])
        def send_welcome(message):
            bot.send_message(
                message.chat.id,
                'Hi, ' + message.from_user.username + '!',
                reply_markup=keyboard())

        @bot.message_handler(content_types=["text"])
        def any_text(message):
            chat_id = message.chat.id
            if message.text == 'Products':
                text = 'Product list:'
                bot.send_message(chat_id, text, reply_markup=products_list_btn())
            if message.text == 'Orders':
                text = 'Orders list:'
                bot.send_message(chat_id, text, reply_markup=orders_list_btn())

        @bot.callback_query_handler(func=lambda message: True)
        def callback_handler(message):
            products = Product.objects.all()
            chat_id = message.message.chat.id
            for product in products:
                if 'product_text' in message.data:
                    if product.name == message.data.split('_')[2]:
                        bot.send_photo(
                            chat_id,
                            open(working_directory + settings.MEDIA_URL + product.preview_image.name, 'rb'),
                            caption="Product name:" + product.name,
                            reply_markup=order_btn(),
                        )
                if 'order_text' in message.data:
                    if product.name == message.data.split('_')[2]:
                        bot.send_photo(
                            chat_id,
                            open(working_directory + settings.MEDIA_URL + product.preview_image.name, 'rb'),
                            caption="Product name:" + product.name,
                            reply_markup=orders_list_btn(),
                        )
                if 'order_product' in message.data:
                    if product.name == message.data.split('_')[2]:
                        create_order(message, product)
                        bot.send_message(chat_id, 'The order has been successfully created!', parse_mode='HTML', reply_markup=keyboard())

            if message.data == 'return_back':
                bot.send_message(chat_id, 'Main menu:', parse_mode='HTML', reply_markup=keyboard())

        def keyboard():
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            btn = types.KeyboardButton('Products')
            btn1 = types.KeyboardButton('Orders')
            markup.add(btn, btn1)
            return markup

        def products_list_btn():
            products = Product.objects.all()
            Keyboard = types.InlineKeyboardMarkup()
            for product in products:
                Keyboard.add(
                    types.InlineKeyboardButton(text=product.name, callback_data="product_text_" + product.name))
            Keyboard.add(types.InlineKeyboardButton(text='Back to main menu', callback_data="return_back"))
            return Keyboard

        def orders_list_btn():
            orders = TelegramOrder.objects.all()
            Keyboard = types.InlineKeyboardMarkup()
            for order in orders:
                Keyboard.add(
                    types.InlineKeyboardButton(text=order.product.name, callback_data="order_text_"+order.product.name))
            Keyboard.add(types.InlineKeyboardButton(text='Back to main menu', callback_data="return_back"))
            return Keyboard

        def order_btn():
            products = Product.objects.all()
            Keyboard = types.InlineKeyboardMarkup()
            for product in products:
                Keyboard.add(
                    types.InlineKeyboardButton(text='Order a product', callback_data="order_product_" + product.name))
            Keyboard.add(types.InlineKeyboardButton(text='Back to main menu', callback_data="return_back"))
            return Keyboard

        def create_order(message, product):
            order = TelegramOrder(product=Product.objects.get(id=product.id), username=message.from_user.username)
            order.save()

        bot.polling(none_stop=True)
