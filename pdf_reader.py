from PyPDF2 import PdfReader


class PdfToText:

    def __init__(self):
        try:
            self.reader = PdfReader('pdf.pdf')
        except FileNotFoundError:
            print('Your pdf file must be named "pdf.pdf"')
            exit(0)

    def get_text(self):
        text = ''
        pages = self.reader.pages
        for page in pages:
            text += (page.extract_text())
        return text

