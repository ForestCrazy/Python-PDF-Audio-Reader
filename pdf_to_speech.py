import PyPDF2
import pyttsx3

from tkinter import *
from tkinter.filedialog import *


def extract_text(filename):
	pdfFileObj = open(filename, "rb")
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

	mytext = ""

	for pageNum in range(pdfReader.numPages):
		pageObj = pdfReader.getPage(pageNum)
		mytext += pageObj.extractText()

	pdfFileObj.close()

	return mytext


def speak_text(text):
	engine = pyttsx3.init()
	engine.setProperty('rate', 150)
	engine.setProperty('voice', 'en+m7')
	engine.say(text)
	engine.runAndWait()


if __name__ == "__main__":
	root = Tk()
	root.withdraw()
	file_path = askopenfilename()
	root.update()
	root.destroy()
	text = extract_text(file_path)
	speak_text(text)