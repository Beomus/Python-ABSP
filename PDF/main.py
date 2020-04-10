import PyPDF2 as pdf 
import os


PDF_DIR = r"C:\Beomus\Codes\Python\PDF\PDF Files"

pdf_writer = pdf.PdfFileWriter()

for file in os.listdir(PDF_DIR):
    pdf_obj = open(f"{PDF_DIR}/{file}", 'rb')
    pdf_reader = pdf.PdfFileReader(pdf_obj)
    for page_num in range(pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page_obj)

pdf_output = open(f"{PDF_DIR}/combined_file.pdf", "wb")
pdf_writer.write(pdf_output)
pdf_output.close()
pdf_obj.close()
