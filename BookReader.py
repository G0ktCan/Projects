import pyttsx3
import PyPDF2


story =open('','rb') 
pdfReader = PyPDF2.PdfFileReader(story)

engine = pyttsx3.init() 
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id) 

for numbers in range(0,pdfReader.numPages):
    s = pdfReader.getPage(numbers)
    text = s.extractText()
    engine.say(text)
    engine.runAndWait()