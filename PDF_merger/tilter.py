import PyPDF2

with open (r"C:\Users\FEDERICO\Documents\Coding\PDF_merger\dummy.pdf", "rb") as file:
    reader = PyPDF2.PdfReader(file)
    print(len(reader.pages))
    page = reader.pages[0].extract_text()
    reader.pages[0].rotate(90)
    writer = PyPDF2.PdfWriter()
    writer.add_page(reader.pages[0])
    with open("rotated_page.pdf", "wb") as new_file:
        writer.write(new_file)