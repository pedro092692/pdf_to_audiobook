from PyPDF2 import PdfReader


class PdfToText:

    def __init__(self):
        self.reader = PdfReader('example.pdf')

    def get_text(self):
        text = ''
        pages = self.reader.pages
        for page in pages:
            text += (page.extract_text())
        return text

