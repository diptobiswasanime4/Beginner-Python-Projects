import pyttsx3
import PyPDF2

book_path = input("Enter book path: ")
book = open(book_path, "rb")
pdf_reader = PyPDF2.PdfFileReader(book)
page_count = pdf_reader.numPages

engine = pyttsx3.init()

page_start = int(input("Enter the starting page to start reading: "))
page = pdf_reader.getPage(page_start)
text = page.extractText()

engine.say(text)
engine.runAndWait()
