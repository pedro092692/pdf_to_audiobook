from txt_to_audio import TextToAudio
from pdf_reader import PdfToText

"""
Your pdf file must be named 'pdf.pdf'
"""

text_to_audio = TextToAudio()
pdf_file = PdfToText()
text = pdf_file.get_text()

if text:
    text_to_audio.create_mp3(text=text)
    print('Your mp3 file was generated')
else:
    print('Sorry there was a problem with pdf file')
