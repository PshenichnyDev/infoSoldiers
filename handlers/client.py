from aiogram import Dispatcher, types
from create_bot import dp
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State
from aiogram.dispatcher.filters.state import StatesGroup

class Register(StatesGroup):
	name = State()
	do = State()

async def startHandler(message : types.message):
	user = message.from_user.username
	msg = f'Привет {user}, хочешь присоеденится к интернет войску? /reg чтобы присоединиться'

	await message.reply(msg)
async def registerHandler(message : types.message):
	await Register.name.set()
	await message.reply('Как вас зовут?')
async def nameHandler(message : types.message, state : FSMContext):
	async with state.proxy() as data:
		data['name'] = message.text
	await Register.next()
	await message.reply('Что вы умеете?')
async def skillsHandler(message : types.message, state : FSMContext):
	async with state.proxy() as data:
		data['skills'] = message.text
	async with state.proxy() as data:
		await message.reply(data.values())
	await state.finish()
	await message.reply('Спасибо за вашу помощь')

def registerHandlersClient(dp : Dispatcher):
	dp.register_message_handler(startHandler, commands = ['start'])
	dp.register_message_handler(registerHandler, commands = ['reg'], state = None)
	dp.register_message_handler(nameHandler, state = Register.name)
	dp.register_message_handler(skillsHandler, state = Register.do)