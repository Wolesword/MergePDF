from PyPDF2 import PdfFileMerger

pdfs = ['1.pdf','2.pdf', '3.pdf', '4.pdf', '5.pdf']

merger = PdfFileMerger(strict=False)

for pdf in pdfs:
    merger.append(pdf)

merger.write("OneFile.pdf")
merger.close()

'''from PyPDF2 import PdfFileMerger
import webbrowser
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

def list_files(directory, extension):
    return (f for f in os.listdir(directory) if f.endswith('.' + extension))

pdfs = list_files(dir_path, "pdf")

merger = PdfFileMerger(strict=False)

for pdf in pdfs:
    merger.append(open(pdf, 'rb'))

with open('results.pdf', 'wb') as fout:
    merger.write(fout)

webbrowser.open_new('file://'+ dir_path + '/result.pdf')'''