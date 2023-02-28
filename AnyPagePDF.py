from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
import os

liste = os.listdir("c:/TMP/test/PDF")
path = ("c:/TMP/test/PDF/")

for i in range(len(liste)):
    print(f"{liste[i]}")

pdfWriter = PdfFileWriter()
for filename in liste:
    pdfFileObject = open(f"{path}{filename}", "rb")
    pdfReader = PdfFileReader(pdfFileObject)
    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

pdfOutput =open("c:/TMP/test/PDF/final2.pdf", "wb")
pdfWriter.write(pdfOutput)
pdfOutput.close()