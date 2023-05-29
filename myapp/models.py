from django.db import models
import aiogram

class Bot(models.Model):
    name = models.CharField(max_length=100)
    token = models.CharField(max_length=100)
    
    async def send_message(self, message):
        bot = aiogram.Bot(token=self.token)
        await bot.send_message(chat_id=self.chat_id, text=message)