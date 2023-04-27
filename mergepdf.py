from PyPDF2 import PdfMerger

pdfs = ["./pdfs/sample1.pdf", "./pdfs/sample2.pdf", "./pdfs/sample3.pdf", "./pdfs/sample4.pdf"]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("./mergedpdf/merged.pdf")
merger.close()