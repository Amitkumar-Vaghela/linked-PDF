# linked-PDF

PDF Merger
This Python script merges multiple PDF files into a single PDF.

Usage
Clone the Repository: Clone this repository to your local machine.
git clone https://github.com/your-username/your-repository.git

Navigate to the Directory: Go to the directory containing the script.
cd your-repository

Install Dependencies: Make sure you have PyPDF2 installed. If not, you can install it via pip:
pip install PyPDF2

Run the Script: Run the script by providing the PDF files you want to merge and specifying the output file name.
python merge_pdfs.py file1.pdf file2.pdf output.pdf
Replace file1.pdf, file2.pdf, and output.pdf with your PDF file names.

Script Details
merge_pdfs(files, output_file): Function to merge multiple PDF files into a single PDF.
files (list): List of PDF files to merge.
output_file (str): Path to the output PDF file.
The script uses PyPDF2 library for PDF manipulation.
Ensure all PDF files are in the same directory as the script or provide the correct paths.
The merged PDF will be created in the same directory as the script.

Example
python merge_pdfs.py document1.pdf document2.pdf merged_document.pdf
This command will merge document1.pdf and document2.pdf into a single PDF named merged_document.pdf.
