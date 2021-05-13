from pywhatkit import text_to_handwriting
import textract as tr

text = tr.process("./doc.docx")

print (text)

text_to_handwriting(text)