from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder

menu = [
    [InlineKeyboardButton(text="💰 найти работу", callback_data="find_job"),
    InlineKeyboardButton(text="🔎 найти видео", callback_data="find_video")],
    [InlineKeyboardButton(text="создать анкету", callback_data="make_anketa"),
    InlineKeyboardButton(text="помощь", callback_data="help")]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])

job = [
    [KeyboardButton(text="like"),
    KeyboardButton(text="skip"),]
]


job_kb = ReplyKeyboardMarkup(keyboard=job)



