import telebot
from django.core.management.base import BaseCommand
from django.apps import apps
from jangoMiniShop import settings
from products.models import Product

bot = telebot.TeleBot(settings.TELEGRAM_API_TOKEN)


class Command(BaseCommand):
    help = 'Telegram Bot'

    def handle(self, *args, **options):
        @bot.message_handler(commands=['products'])
        def start_message(message):
            products = Product.objects.all()
            for product in products:
                bot.send_message(message.chat.id, product.name)

        bot.polling()
