# keyboards.py

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data import cities


def cities_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=city, callback_data=f"city_{city}")]
            for city in cities
        ]
    )


def back_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⬅️ Zurück", callback_data="back")]
        ]
    )


def filter_kb(city):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🚚 Nur Lieferung", callback_data=f"filter_{city}")],
            [InlineKeyboardButton(text="⬅️ Zurück", callback_data="back")]
        ]
    )


def sponsor_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📢 Kanal beitreten",
                    url="https://t.me/HalalEssenDE"  # ← ИНРО БА КАНАЛИ ХУД ИВАЗ КУН
                )
            ],
            [
                InlineKeyboardButton(
                    text="✅ Ich habe abonniert",
                    callback_data="check_sub"
                )
            ]
        ]
    )