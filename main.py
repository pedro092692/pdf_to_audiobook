from txt_to_audio import TextToAudio

text_to_audio = TextToAudio()

with open('text.txt', mode='r', encoding='utf-8') as file:
    text = file.read()

print(text)

text_to_audio.create_mp3(text=text)