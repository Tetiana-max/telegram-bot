from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Вставте ваш токен сюди
TOKEN = "7736790245:AAEPjiRHrm1gmmxnEVBycmy4gyAUso-6QOA"

# Вставте ID вашої групи
GROUP_ID = -1002416651558  # Замініть на реальний ID вашої групи

# Ініціалізація бота
app = Application.builder().token(TOKEN).build()

# Обробка повідомлень, надісланих напряму боту
async def forward_to_group(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Перевіряємо, чи повідомлення надіслано напряму боту
    if update.message.chat.type == "private":
        user_message = update.message.text
        user_name = update.message.from_user.full_name
        # Пересилаємо повідомлення в групу
        await context.bot.send_message(
            chat_id=GROUP_ID,
            text=f"Повідомлення від {user_name}:\n{user_message}"
        )
        # Відповідаємо відправнику
        await update.message.reply_text("Ваше повідомлення надіслано в групу!")

# Додаємо обробник повідомлень
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_group))

# Запуск бота
if __name__ == "__main__":
    print("Бот запущений...")
    app.run_polling()
