from aiogram.utils import executor
from create_bot import dp
from handlers import client

client.registerHandlersClient(dp)

executor.start_polling(dp, skip_updates = True)