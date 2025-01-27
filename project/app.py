import gradio as gr
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

# Define functions for PDF processing and querying
def extract_text_from_pdf(pdf_file):
    try:
        # Debug print file details
        print(f"File type: {type(pdf_file)}")
        print(f"File name: {pdf_file.name}")
        print(f"File size: {os.path.getsize(pdf_file.name)} bytes")
        
        # Open and read the file
        with open(pdf_file.name, 'rb') as file:
            reader = PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            print(f"Extracted text length: {len(text)}")  # Debug print
            return text
    except Exception as e:
        print(f"Error in extract_text_from_pdf: {str(e)}")
        raise

def split_text(text, chunk_size=500):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def build_faiss_index(chunks, model_name='all-MiniLM-L6-v2'):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(chunks, convert_to_tensor=False)
    dim = embeddings[0].shape[0]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    return index, chunks

def query_faiss(index, query, chunks, model_name='all-MiniLM-L6-v2'):
    model = SentenceTransformer(model_name)
    query_embedding = model.encode([query], convert_to_tensor=False)
    distances, indices = index.search(np.array(query_embedding), k=3)
    return [chunks[i] for i in indices[0]]

# Create the Gradio app
def rag_lite_app(pdf_file, query):
    if not pdf_file or not query:
        return "Please upload a PDF file and enter a query."
    try:
        print(f"Processing PDF file: {pdf_file.name}")
        
        # Validate file exists and is not empty
        if not os.path.exists(pdf_file.name):
            return "File does not exist"
        if os.path.getsize(pdf_file.name) == 0:
            return "File is empty"
            
        text = extract_text_from_pdf(pdf_file)
        if not text:
            return "No text could be extracted from the PDF"
            
        print(f"Extracted text length: {len(text)}")
        chunks = split_text(text)
        print(f"Number of chunks: {len(chunks)}")
        index, chunks = build_faiss_index(chunks)
        results = query_faiss(index, query, chunks)
        return "\n\n--- Relevant Excerpt ---\n\n".join(results)
    except Exception as e:
        print(f"Error processing request: {str(e)}")
        return f"An error occurred: {str(e)}"

# Define Gradio interface
interface = gr.Interface(
    fn=rag_lite_app,
    inputs=[
        gr.File(
            label="Upload PDF",
            type="file",
            file_types=[".pdf"]
        ),
        gr.Textbox(
            label="Enter Your Query",
            placeholder="What would you like to know about the document?"
        )
    ],
    outputs=gr.Textbox(label="Results", lines=10),
    title="RAG-lite PDF Query App",
    description="Upload a PDF document and ask questions about its content.",
    examples=[
        ["tutorial/sample_docs/financial_report.pdf", "What was the revenue in Q4 2023?"],
        ["tutorial/sample_docs/trading_document.pdf", "What are the main trading strategies?"]
    ],
    allow_flagging="manual",
    flagging_options=["Issue", "Wrong Answer", "Other"]
)

# Launch the app
interface.launch()
