import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Habilitar el registro de eventos de Telegram
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Reemplaza la siguiente línea con tu token real.
# Por favor, asegúrate de que esté entre comillas.
BOT_TOKEN = "8336734664:AAG0aus6_QZjL1uvo5LgYIzWciOEhAwZh7o"

# Define una función para manejar el comando /start
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envía un mensaje cuando se emite el comando /start."""
    user = update.effective_user
    await update.message.reply_html(
        f"Hola {user.mention_html()}! 👋"
    )

def main() -> None:
    """Inicia el bot."""
    # Crea el objeto Application y pásale el token del bot
    application = Application.builder().token(BOT_TOKEN).build()

    # Añade el handler para el comando /start
    application.add_handler(CommandHandler("start", start_command))

    # Inicia el polling para recibir mensajes
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()