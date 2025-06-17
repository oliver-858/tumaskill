from app import app
from flask import request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import os
from datetime import datetime, timedelta
import json
from dotenv import load_dotenv

load_dotenv()

# WhatsApp webhook endpoint
@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get("Body", "").strip().lower()
    sender = request.values.get("From", "")

    # Create Twilio response object
    response = MessagingResponse()
    msg = response.message()

    # Basic command recognition
    if incoming_msg in ["hi", "hello", "hey"]:
        msg.body("hello naitwa oliver kogi Karibu TumaSkill 👋\n\nChoose your language:\n1. English\n2. Kiswahili\n3. Sheng")
    elif incoming_msg == "1":
        msg.body("You've selected English 🇬🇧.\n\nType 'start' to begin your course.")
    elif incoming_msg == "2":
        msg.body("Umechagua Kiswahili 🇰🇪.\n\nAndika 'anza' kuanza masomo yako.")
    elif incoming_msg == "3":
        msg.body("Umechagua Sheng 😎.\n\nTipe 'anza' tukusort masomo fiti.")
    elif incoming_msg in ["start", "anza"]:
        msg.body("🧠 Lesson 1: Introduction to the Kenya Online Market.\n\nThe online space in Kenya is growing fast. Many youth are making money through Jumia, Instagram, and TikTok.\n\nType 'next' to continue.")
    elif incoming_msg == "next":
        msg.body("📲 Lesson 2: What You Need to Start\n\nAll you need is a smartphone, bundles, and consistency.\n\nMore lessons coming soon... 🛠️")
    else:
        msg.body("Sorry 😓 I didn’t understand that. Type 'hi' to begin.")

    return str(response)

