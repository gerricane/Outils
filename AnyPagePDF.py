from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
import os

liste = os.listdir("c:/TMP/test/PDF")
path = ("c:/TMP/test/PDF/")
path_output = input("Donnez un nom de fichier de sortie, sans l'extension .pdf: ")

for i in range(len(liste)):
    print(f"{liste[i]}")

pdfWriter = PdfFileWriter()
for filename in liste:
    pdfFileObject = open(f"{path}{filename}", "rb")
    pdfReader = PdfFileReader(pdfFileObject)
    for pageNum in range(0,1):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

pdfOutput = open(f"{path}{path_output}.pdf", "wb")
pdfWriter.write(pdfOutput)
pdfOutput.close()