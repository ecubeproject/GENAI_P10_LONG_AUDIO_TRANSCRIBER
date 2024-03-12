from openai import OpenAI
from pydub import AudioSegment
import config

client = OpenAI(api_key=config.API_KEY)
AudioSegment.converter = "/usr/bin/ffmpeg"
song = AudioSegment.from_mp3("audio_files/phone.mp3")
# 5 minute portion
five_minutes = 5 * 60 * 1000
first_min_5 = song[:five_minutes]
first_min_5.export("audio_files/phone_first_5.mp3", format="mp3")
last_min_5 = song[five_minutes:]
last_min_5.export("audio_files/phone_last_5.mp3", format="mp3")
file1 = open("audio_files/phone_first_5.mp3", "rb")
result = client.audio.transcriptions.create(model="whisper-1", file=file1)
print(result)
file2 = open("audio_files/phone_last_5.mp3", "rb")
result = client.audio.transcriptions.create(model="whisper-1", file=file2)
print(result)
