import requests
from aiogram import types, executor, Bot, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from environs import Env

env = Env()
env.read_env()

TOKEN = env.str('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot)

kb_rwb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('/register'),
            KeyboardButton('/view'),
            KeyboardButton('/delete')
        ]
    ], resize_keyboard=True
)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(f'Hello @{message.from_user.username}', reply_markup=kb_rwb)


@dp.message_handler(commands=['register'])
async def cmd_register(message: types.Message):
    user_data = {
        'tg_id': message.from_user.id,
        'full_name': message.from_user.full_name,
        'username': message.from_user.username,
        'language': message.from_user.language_code
    }
    try:
        response = requests.post('http://127.0.0.1:8000/api/v1/users/', json=user_data)
        if response.status_code == 201:
            await message.answer('Your data has been added to the database.')
        elif response.status_code == 400:
            await message.answer("You are already in the database!")
        else:
            await message.answer(f'Status code: {response.status_code}')
    except Exception as e:
        await message.answer(f"Error: {e}")


@dp.message_handler(commands=['view'])
async def cmd_view(message: types.Message):
    try:
        response = requests.get(f'http://127.0.0.1:8000/api/v1/users/')

        if response.status_code == 200:
            for users in response.json():
                print(users)
                for user in users:
                    print(user)
                    if message.from_user.id in user['tg_id']:
                        await message.answer(f'tg_id: {user["tg_id"]}\n'
                                             f'full_name:  {user["full_name"]}\n'
                                             f'username:  {user["username"]}\n'
                                             f'language:  {user["language"]}\n')
                        break
                else:
                    await message.answer("Your data was not found in the database.")
        else:
            await message.answer(f'Status code: {response.status_code}')
    except Exception as e:
        await message.answer(f"Error: {e}")


@dp.message_handler(commands=['delete'])
async def cmd_delete(message: types.Message):
    user_id = message.from_user.id
    try:

        response = requests.delete(f'http://127.0.0.1:8000/api/v1/users/delete/{user_id}/')
        if response.status_code == 204:
            await message.answer('Your data has been deleted from the database.')
        elif response.status_code == 404:
            await message.answer("You are not in the database!")
        else:
            await message.answer(f'Status code: {response.status_code}')
    except Exception as e:
        await message.answer(f"Error: {e}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
