import os
from PyPDF2 import PdfReader

def verify_pdf(pdf_path):
    try:
        print(f"Checking file: {pdf_path}")
        print(f"File exists: {os.path.exists(pdf_path)}")
        print(f"File size: {os.path.getsize(pdf_path)} bytes")
        
        with open(pdf_path, 'rb') as file:
            reader = PdfReader(file)
            print(f"Number of pages: {len(reader.pages)}")
            
            # Try to extract text from first page
            text = reader.pages[0].extract_text()
            print(f"First page text length: {len(text)}")
            print("First 100 characters:", text[:100])
            
    except Exception as e:
        print(f"Error verifying PDF: {str(e)}")

if __name__ == "__main__":
    verify_pdf("tutorial/sample_docs/financial_report.pdf")
    verify_pdf("tutorial/sample_docs/trading_document.pdf") 