import PyPDF2
import sys

input_files = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        print(pdf)
        with open(pdf, "rb") as file:
            merger.append(PyPDF2.PdfReader(file))
    merger.write("super.pdf")

pdf_combiner(input_files)