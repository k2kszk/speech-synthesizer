#./advance/main.py
from flask import Flask
from flask import render_template
from flask import request
from flask import send_file
import os
from google.cloud import texttospeech

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        if request.form['Radio'] == 'normal':
            ssml = '<speak><prosody rate="slow">' + request.form['text'] + '</prosody></speak>'
        else:
            ssml = '<speak>' + request.form['text'] + '</speak>'

        accent = request.form['accent']
        voiceid = next(voice for voice in request.form.getlist('voiceId[]') if accent in voice)
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="credentials.json"
 
        client = texttospeech.TextToSpeechClient()
        input_text = texttospeech.types.SynthesisInput(ssml=ssml)
        voice = texttospeech.types.VoiceSelectionParams(
            language_code=accent,
            name=voiceid)

        audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3)

        response = client.synthesize_speech(input_text, voice, audio_config)

        # The response's audio_content is binary.
        with open('/tmp/output.mp3', 'wb') as out:
            out.write(response.audio_content)

        return send_file("/tmp/output.mp3",as_attachment=True)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run()