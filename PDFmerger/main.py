from PyPDF2 import PdfMerger

pdfs = ['sample-1.pdf', 'sample-2.pdf', 'sample-3.pdf', 'sample-4.pdf']

merger = PdfMerger()

'''merger.append(pdf, pages=(0, 3))     first 3 pages
   merger.append(pdf, pages=(0, 6, 2))   pages 1,3, 5'''

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()