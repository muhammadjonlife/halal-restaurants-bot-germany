from aiogram import Router, types, F, Bot
from aiogram.filters import Command
import os

from data import restaurants
from keyboards import cities_kb, back_kb, filter_kb, sponsor_kb

router = Router()

CHANNEL_ID = "@HalalEssenDE"
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

# ===== USERS =====
def save_user(user_id):
    with open("users.csv", "a") as f:
        f.write(str(user_id) + "\n")


def get_users():
    try:
        with open("users.csv", "r") as f:
            return list(set([int(line.strip()) for line in f]))
    except:
        return []


# ===== SUB CHECK =====
async def check_subscription(bot: Bot, user_id: int) -> bool:
    try:
        member = await bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status not in ("left", "kicked")
    except:
        return False


# ===== FORMAT =====
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


# ===== START =====
@router.message(Command("start"))
async def start(msg: types.Message, bot: Bot):
    save_user(msg.from_user.id)

    is_sub = await check_subscription(bot, msg.from_user.id)

    if not is_sub:
        await msg.answer(
            "❌ Du musst zuerst den Kanal abonnieren!",
            reply_markup=sponsor_kb()
        )
        return

    await msg.answer("🇩🇪 Wähle eine Stadt:", reply_markup=cities_kb())


# ===== CHECK BUTTON =====
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


# ===== CITY =====
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


# ===== FILTER =====
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


# ===== BACK =====
@router.callback_query(F.data == "back")
async def back(callback: types.CallbackQuery):
    await callback.message.answer(
        "🔙 Zurück zum Menü:",
        reply_markup=cities_kb()
    )


# ===== ADMIN =====
@router.message(Command("admin"))
async def admin_panel(msg: types.Message):
    if msg.from_user.id != ADMIN_ID:
        return

    await msg.answer("👨‍💼 Admin Panel:\n\n/stats\n/broadcast")


# ===== STATS =====
@router.message(Command("stats"))
async def stats(msg: types.Message):
    if msg.from_user.id != ADMIN_ID:
        return

    users = get_users()
    await msg.answer(f"📊 Users: {len(users)}")


# ===== BROADCAST =====
waiting_broadcast = set()


@router.message(Command("broadcast"))
async def broadcast_start(msg: types.Message):
    if msg.from_user.id != ADMIN_ID:
        return

    waiting_broadcast.add(msg.from_user.id)
    await msg.answer("✍️ Nachricht eingeben:")


@router.message(F.text)
async def handle_text(msg: types.Message, bot: Bot):
    # 👉 broadcast режим
    if msg.from_user.id in waiting_broadcast:
        users = get_users()
        success = 0

        for user_id in users:
            try:
                await bot.send_message(user_id, msg.text)
                success += 1
            except:
                pass

        await msg.answer(f"✅ Gesendet: {success}")
        waiting_broadcast.remove(msg.from_user.id)
        return

    # 👉 search
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