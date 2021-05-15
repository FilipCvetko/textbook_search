from pathlib import Path
import PyPDF2

file = 'textbook_pdfs/robbins.pdf'

reader = PyPDF2.PdfFileReader(file)
out = reader.getPage(300)

out.mediaBox.lowerLeft = (150, 150)
out.mediaBox.upperRight = (400, 400)

from pdfminer.high_level import extract_text

text = extract_text(file, page_numbers=[300])
print(text)



writer = PyPDF2.PdfFileWriter()
writer.addPage(out)

with open("haha.pdf", "wb") as file:
    writer.write(file)