from aiogram import F, Router, types, Bot
from aiogram.filters import Command
from aiogram.fsm import state
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
import sqlite3
import config
import kb
import text


class UserState(StatesGroup):
    input = State()


router = Router()


bot = Bot(token=config.BOT_TOKEN)


@router.message(Command("start"))
async def start_handler(msg: Message):
    conn = sqlite3.connect('tele.db')
    cursor = conn.cursor()

    cursor.execute('Create table if not exists user(id int auto_increment primary key,userid int,data text,count int)')
    conn.commit()
    cursor.close()
    conn.close()

    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)


@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)


@router.callback_query(F.data == "find_job")
async def find(msg: Message, state: FSMContext):
    await state.set_state(input())
    await bot.send_message(msg.from_user.id, text.job_start, reply_markup=kb.job_kb)


@router.message(state=UserState.input)
async def search(msg: Message, state: FSMContext):
    await state.update_data(input=msg.text)
    await bot.send_message(msg.from_user.id, "здарова, {html.quote(msg.text)}!\n")

