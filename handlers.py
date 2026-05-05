# handlers.py

from aiogram import Router, types, F, Bot
from aiogram.filters import Command

from data import restaurants
from keyboards import cities_kb, back_kb, filter_kb, sponsor_kb

router = Router()

CHANNEL_ID = "@HalalEssenDE"


# ✅ FINAL FIX — works for member/admin/owner
async def check_subscription(bot: Bot, user_id: int) -> bool:
    try:
        member = await bot.get_chat_member(CHANNEL_ID, user_id)

        # accept everyone except left / kicked
        return member.status not in ("left", "kicked")

    except Exception as e:
        print("SUB CHECK ERROR:", e)
        return False


# 🔥 Format restaurant красиво
def format_restaurant(r):
    menu = "\n".join([f"  • {m['name']} — {m['price']}" for m in r["menu"]])

    return (
        f"🍽 <b>{r['name']}</b>\n"
        f"📍 {r['address']}\n"
        f"📞 {r['phone']}\n"
        f"🚚 Lieferung: {'Ja' if r['delivery'] else 'Nein'}\n\n"
        f"📋 <b>Menü:</b>\n{menu}\n\n"
        f"🔗 <a href='{r['link']}'>Google Maps</a>\n"
        f"━━━━━━━━━━━━━━━\n"
    )


# 🚀 START
@router.message(Command("start"))
async def start(msg: types.Message, bot: Bot):
    is_sub = await check_subscription(bot, msg.from_user.id)

    if not is_sub:
        await msg.answer(
            "❌ Du musst zuerst den Kanal abonnieren!",
            reply_markup=sponsor_kb()
        )
        return

    await msg.answer("🇩🇪 Wähle eine Stadt:", reply_markup=cities_kb())


# 🔁 CHECK BUTTON
@router.callback_query(F.data == "check_sub")
async def check_sub(callback: types.CallbackQuery, bot: Bot):
    is_sub = await check_subscription(bot, callback.from_user.id)

    if is_sub:
        await callback.message.answer(
            "✅ Zugang erlaubt\n\n🇩🇪 Wähle eine Stadt:",
            reply_markup=cities_kb()
        )
    else:
        await callback.answer("❌ Du bist noch nicht abonniert", show_alert=True)


# 📍 CITY SELECT
@router.callback_query(F.data.startswith("city_"))
async def show_city(callback: types.CallbackQuery):
    city = callback.data.split("_")[1]
    data = restaurants.get(city, [])

    text = f"📍 <b>{city}</b>\n\n"

    for r in data:
        text += format_restaurant(r)

    await callback.message.answer(
        text,
        reply_markup=filter_kb(city),
        parse_mode="HTML"
    )


# 🚚 FILTER DELIVERY
@router.callback_query(F.data.startswith("filter_"))
async def filter_delivery(callback: types.CallbackQuery):
    city = callback.data.split("_")[1]
    data = [r for r in restaurants.get(city, []) if r["delivery"]]

    if not data:
        await callback.message.answer("❌ Keine Lieferung verfügbar")
        return

    text = f"🚚 <b>Nur Lieferung in {city}</b>\n\n"

    for r in data:
        text += format_restaurant(r)

    await callback.message.answer(
        text,
        reply_markup=back_kb(),
        parse_mode="HTML"
    )


# 🔙 BACK
@router.callback_query(F.data == "back")
async def back(callback: types.CallbackQuery):
    await callback.message.answer(
        "🔙 Zurück zum Menü:",
        reply_markup=cities_kb()
    )


# 🔍 SEARCH (TEXT INPUT)
@router.message()
async def search(msg: types.Message):
    query = msg.text.lower()
    results = []

    for city, items in restaurants.items():
        for r in items:
            if query in r["name"].lower():
                results.append((city, r))

    if not results:
        await msg.answer("❌ Nichts gefunden")
        return

    text = "🔍 <b>Suchergebnisse:</b>\n\n"

    for city, r in results:
        text += f"📍 {city}\n{format_restaurant(r)}"

    await msg.answer(text, parse_mode="HTML")