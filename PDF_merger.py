''' Merger of five PDF's '''

from PyPDF2 import PdfFileMerger

pdfs = ['1.pdf','2.pdf', '3.pdf', '4.pdf', '5.pdf']

merger = PdfFileMerger(strict=False)

for pdf in pdfs:
    merger.append(pdf)

merger.write("OneFile.pdf")
merger.close()