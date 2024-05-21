import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from api_test import *

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "7058792123:AAFEGbCT-9xnv28n5J3sADjZrJk4ZJm2v6U"

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message(Command('posts'))
async def posts_handler(message: Message) -> None:
    try:
        datas = get_all_posts()
        # logging.info(datas)
        # logging.info(type(datas))
        if datas:
            for data in datas:
                text = (f"title: {data['title']}\n"
                        f"content: {data['content']}\n"
                        f"rasm: <a href='{data['image']}'>Rasm</a>\n")

                if data['image']:
                    await message.answer_photo(photo=data['image'], caption=text)
                else:
                    await message.answer(text)
        else:
            await message.answer("Ma'lumot kiriting: ")
    except ConnectionError as e:
        await message.answer("Nice Try! ")

@dp.message(Command("users"))
async def users_handler(message: Message) -> None:
    try:
        datas = get_all_users()

        if datas:
            for data in datas:
                text = (
                    f"url: {data['url']}\n"
                    f"username: {data['username']}\n"
                    f"email: {data['email']}\n"
                    f"is_staff: {data['is_staff']}\n"
                    f"is_active: {data['is_active']}\n"
                    f"is_superuser: {data['is_superuser']}\n")
                await message.answer(text)
        else:
            await message.answer("Malumot kiriting: ")
    except ConnectionError as e:
        await message.answer("Nice try !")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())