from PyPDF2 import PdfWriter, PdfReader
import os

def merge_pdfs(files, output_file):
    """
    Merge multiple PDF files into a single PDF.

    Args:
        files (list): List of PDF files to merge.
        output_file (str): Path to the output PDF file.
    """
    merger = PdfWriter()

    # Loop through each PDF file
    for pdf_file in files:
        if pdf_file.endswith(".pdf"):
            # Open each PDF file and add its pages to the merger
            with open(pdf_file, "rb") as file:
                reader = PdfReader(file)
                merger.add_pages(reader.pages)

    # Write the merged PDF to the output file
    with open(output_file, "wb") as output:
        merger.write(output)

    # Close the merger
    merger.close()

# Get a list of PDF files in the current directory
pdf_files = [file for file in os.listdir() if file.endswith(".pdf")]

# Specify the output file name for the merged PDF
output_pdf = "merged_pdf.pdf"

# Merge the PDF files
merge_pdfs(pdf_files, output_pdf)

print("PDF files merged successfully!")
