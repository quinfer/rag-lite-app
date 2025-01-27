# RAG-lite PDF Query App Tutorial

This tutorial will guide you through using the RAG-lite PDF Query App to extract insights from your PDF documents.

## Getting Started

1. **Upload a Document**
   - Click the "Upload PDF" button
   - Select any PDF document from your computer
   - The app will process the document and create searchable embeddings

2. **Query Your Document**
   - Type your question in the query box
   - The app will return the most relevant passages from your document
   - You'll receive 3 most relevant text chunks as results

## Sample Documents

In the `sample_docs` folder, you'll find two example documents:
- `financial_report.pdf`: A sample financial report
- `trading_document.pdf`: A sample trading strategy document

## Example Queries

Try these example queries with the sample documents:

For financial_report.pdf:
- "What were the key financial metrics for Q4?"
- "Describe the revenue growth trends"

For trading_document.pdf:
- "What are the main trading strategies discussed?"
- "Explain the risk management approach"

## Tips for Better Results

1. Be specific in your queries
2. Use complete sentences for better semantic matching
3. Try reformulating your question if the initial results aren't satisfactory

## Limitations

- The app processes text in chunks of 500 characters
- Only text content is processed (images and tables are ignored)
- The app returns the 3 most relevant chunks per query 