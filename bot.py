import os
from telegram import Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes
import logging

# Configuration du logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Remplacez 'VOTRE_TOKEN_BOT' par le token de votre bot Telegram
TOKEN = '7174970942:AAHA8Qd-Y8-UOLkL-9OtkIcY-topbUi4kuo'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Gère la commande /start et affiche le bouton pour lancer la mini-app"""
    await update.message.reply_text(
        "Bienvenue sur QuizMaster ! 🎓\n"
        "Cliquez sur le bouton ci-dessous pour commencer le quiz.",
        reply_markup={
            "inline_keyboard": [[
                {
                    "text": "🎮 Lancer le quiz",
                    "web_app": {"url": "https://abdine24.github.io/quiz/"}
                }
            ]]
        }
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Gère la commande /help"""
    await update.message.reply_text(
        "Préparation concours est une application de quiz interactive !\n\n"
        "Commandes disponibles:\n"
        "/start - Démarrer le quiz\n"
        "/help - Afficher ce message d'aide"
    )

def main():
    """Fonction principale qui démarre le bot"""
    # Création de l'application
    application = Application.builder().token(TOKEN).build()

    # Ajout des handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Démarrage du bot
    application.run_polling()

if __name__ == '__main__':
    main() 