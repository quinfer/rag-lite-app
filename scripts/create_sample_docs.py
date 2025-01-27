import pypandoc
import os

# Create directories if they don't exist
os.makedirs('tutorial/sample_docs', exist_ok=True)

# Convert markdown files to PDFs
def convert_to_pdf():
    # Convert Q4 Financial Report
    pypandoc.convert_file(
        'Q4 Financial Report - Nippers Global Corp.md',
        'pdf',
        outputfile='tutorial/sample_docs/financial_report.pdf',
        format='markdown'
    )
    
    # Convert Trading Strategy document
    pypandoc.convert_file(
        'Trading Strategy Insights - TrendTracker Ltd.md',
        'pdf',
        outputfile='tutorial/sample_docs/trading_document.pdf',
        format='markdown'
    )

if __name__ == "__main__":
    convert_to_pdf() 