from PyPDF2 import PdfMerger

pdfs = ["sample1.pdf", "sample2.pdf", "sample3.pdf", "sample4.pdf"]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()