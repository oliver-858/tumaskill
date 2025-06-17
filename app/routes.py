from app import app
from flask import request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Root route for Render health check
@app.route('/')
def index():
    return 'TumaSkill WhatsApp bot is running! ✅'

# WhatsApp webhook endpoint
@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    # Get incoming WhatsApp message
    incoming_msg = request.values.get("Body", "").strip().lower()
    sender = request.values.get("From", "")

    # Initialize Twilio MessagingResponse
    response = MessagingResponse()
    msg = response.message()

    # Basic conversation flow
    if incoming_msg in ["hi", "hello", "hey"]:
        msg.body(
            "hello naitwa Oliver Kogi 😎 Karibu TumaSkill 👋\n\n"
            "Choose your language:\n"
            "1. English 🇬🇧\n"
            "2. Kiswahili 🇰🇪\n"
            "3. Sheng 🔥"
        )
    elif incoming_msg == "1":
        msg.body("You've selected English 🇬🇧.\n\nType 'start' to begin your course.")
    elif incoming_msg == "2":
        msg.body("Umechagua Kiswahili 🇰🇪.\n\nAndika 'anza' kuanza masomo yako.")
    elif incoming_msg == "3":
        msg.body("Umechagua Sheng 😎.\n\nTipe 'anza' tukusort masomo fiti.")
    elif incoming_msg in ["start", "anza"]:
        msg.body(
            "🧠 Lesson 1: Introduction to the Kenya Online Market.\n\n"
            "The online space in Kenya is growing fast. Many youth are making money "
            "through Jumia, Instagram, and TikTok.\n\n"
            "Type 'next' to continue."
        )
    elif incoming_msg == "next":
        msg.body(
            "📲 Lesson 2: What You Need to Start\n\n"
            "All you need is a smartphone, bundles, and consistency.\n\n"
            "More lessons coming soon... 🛠"
        )
    else:
        msg.body("😓 Sorry, I didn’t understand that. Type 'hi' to begin.")

    return str(response)

