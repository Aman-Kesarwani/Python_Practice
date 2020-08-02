import PyPDF2

with open(r"D:\Upgrad_\document.pdf", "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
# open(r"D:\Upgrad_\LIC_28000.pdf")
    print(reader.numPages)
    page = reader.getPage(0)
    page.rotateClockwise(90)

    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)

    with open("rotated.pdf", "wb") as output:
        writer.write(output)

# multiple PDFS

merger = PyPDF2.PdfFileMerger()
file_names = [r"D:\Upgrad_\document.pdf", r"D:\Upgrad_\LIC_28000.pdf"]

for file_name in file_names:
    merger.append(file_name)

merger.write("combined.pdf")
