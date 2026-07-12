# voice_processor.py
import requests
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment

#AudioSegment.converter = r"ffmpeg.exe"
#AudioSegment.converter = r"temp_audio/incoming.ogg"  # Ensure ffmpeg is installed and accessible

def download_whatsapp_media(media_url, twilio_sid, twilio_auth_token, output_path):
    """Downloads an audio recording directly from incoming Twilio media streams."""
    response = requests.get(media_url, auth=(twilio_sid, twilio_auth_token))
    if response.status_code == 200:
        with open(output_path, 'wb') as file:
            file.write(response.content)
        return True
    return False


def convert_ogg_to_wav(ogg_path, wav_path):
    """Converts native WhatsApp OGG voice formats into standard uncompressed WAV audio."""
    try:
        audio = AudioSegment.from_ogg(ogg_path)
        audio.export(wav_path, format="wav")
        return True
    except Exception as e:
        print(f"Audio conversion failed: {e}")
        return False


def voice_to_text(wav_path):
    """Converts spoken inputs to text records via audio transcription frameworks."""
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError as e:
        print(e)
        return ""
    except sr.RequestError as e:
        print(e)
        return ""


def text_to_voice(text_content, output_audio_path):
    """Synthesizes text back into voice-based audible outputs[cite: 1]."""
    tts = gTTS(text=text_content, lang='en', tld='co.ke')
    tts.save(output_audio_path)
