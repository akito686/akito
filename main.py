import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Біо", callback_data='bio')],
        [InlineKeyboardButton("Портфоліо + всі фото", callback_data='portfolio')],
        [InlineKeyboardButton("Відгуки + всі фото", callback_data='reviews')],
        [InlineKeyboardButton("Що можна замовити і прайс", callback_data='services')],
        [InlineKeyboardButton("Написати мені", callback_data='chat')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Привіт! Обирай:', reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'bio':
        await query.edit_message_text(
            text="Привіт! Я дизайнер Akito. Займаюся створенням унікальних логотипів, сайтів та ілюстрацій."
        )
    elif query.data == 'portfolio':
        media = [InputMediaPhoto(f"https://example.com/portfolio/{i}.jpg") for i in range(1, 11)]
        await query.delete_message()
        await context.bot.send_media_group(chat_id=query.message.chat_id, media=media)
        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text="Повне портфоліо та більше фото тут: https://твій_профіль"
        )
    elif query.data == 'reviews':
        media = [InputMediaPhoto(f"https://example.com/reviews/{i}.jpg") for i in range(1, 11)]
        await query.delete_message()
        await context.bot.send_media_group(chat_id=query.message.chat_id, media=media)
        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text="Всі відгуки тут: https://твій_сайт"
        )
    elif query.data == 'services':
        await query.edit_message_text(
            text=(
                "📌 Що можна замовити і прайс:\n"
                "1. Логотип — від 1000 грн\n"
                "2. Фірмовий стиль — від 3000 грн\n"
                "3. Дизайн сайту — від 5000 грн\n"
                "4. Ілюстрації — від 1500 грн\n"
                "5. Поліграфія — від 2000 грн\n\n"
                "Більше — на сайті: https://твій_сайт"
            )
        )
    elif query.data == 'chat':
        await query.edit_message_text(text="Напиши мені в Telegram: https://t.me/akito_bio")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Бот запущений…")
    app.run_polling()
