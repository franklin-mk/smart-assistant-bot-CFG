# app.py
import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv

from grammar_rules import parse_query
from responses import get_simulated_response
from voice_processor import (
    download_whatsapp_media,
    convert_ogg_to_wav,
    voice_to_text,
    text_to_voice
)

# Load the environment variables from the .env file
load_dotenv()

app = Flask(__name__)

# Access the variables safely using os.environ.get()
TWILIO_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

# Temporary local tracking directory
UPLOAD_DIR = os.path.join(os.getcwd(), "temp_audio")
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.route("/whatsapp", methods=['POST'])
def whatsapp_webhook():
    incoming_msg = request.values.get('Body', '').strip()
    media_url = request.values.get('MediaUrl0', None)

    response = MessagingResponse()
    msg = response.message()

    # Voice input processing logic
    if media_url:
        ogg_file = os.path.join(UPLOAD_DIR, "incoming.ogg")
        wav_file = os.path.join(UPLOAD_DIR, "incoming.wav")

        if download_whatsapp_media(media_url, TWILIO_SID, TWILIO_AUTH_TOKEN, ogg_file):
            if convert_ogg_to_wav(ogg_file, wav_file):
                transcribed_text = voice_to_text(wav_file)

                if transcribed_text:
                    intent = parse_query(transcribed_text)
                    reply_text = get_simulated_response(intent)

                    output_voice = os.path.join(UPLOAD_DIR, "response.mp3")
                    text_to_voice(reply_text, output_voice)

                    msg.body(f"Transcribed Query: '{
                             transcribed_text}'\n\n{reply_text}")
                else:
                    msg.body(
                        "Sorry, I could not understand the audio clearly. Please write your query down.")
            else:
                msg.body("System error converting student audio note.")
        else:
            msg.body("Could not download your audio files from WhatsApp servers.")

    # Text input processing logic
    else:
        intent = parse_query(incoming_msg)
        reply_text = get_simulated_response(intent)
        msg.body(reply_text)

    return str(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
