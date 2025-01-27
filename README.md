   ---
   title: "RAG-lite-app"
   emoji: 🚀
   colorFrom: "blue"
   colorTo: "indigo"
   sdk: "gradio"
   app_file: "app.py"s
   pinned: false
   ---

# RAG-lite PDF Query App

A simple RAG (Retrieval Augmented Generation) application that allows users to query PDF documents. This app is designed to help students and researchers efficiently extract information from PDF documents using natural language queries.

## Live Demo
Try the app at [Hugging Face Spaces](https://huggingface.co/spaces/quinfer/rag-lite-app)

## Features
- **PDF Document Upload**: Upload any PDF document for analysis
- **Natural Language Queries**: Ask questions about the document in plain English
- **Smart Retrieval**: Uses FAISS for efficient similarity search
- **Relevant Excerpts**: Get specific, contextual answers from the document
- **User Feedback**: Flag issues or incorrect answers for continuous improvement
- **Sample Documents**: Pre-loaded examples to try the system

## Sample Documents
The app comes with two sample documents:
1. **Financial Report** - Q4 2023 report from Nippers Global Corp
   - Example queries:
     - "What was the revenue in Q4 2023?"
     - "How has revenue grown over the past quarters?"
     - "What is the regional revenue distribution?"

2. **Trading Document** - Trading strategies from TrendTracker Ltd
   - Example queries:
     - "What are the main trading strategies?"
     - "Explain the position sizing approach"
     - "What are the portfolio risk controls?"

## Technology Stack
Built with:
- **Gradio**: For the web interface
- **PyPDF2**: PDF text extraction
- **Sentence Transformers**: Document and query embedding
- **FAISS**: Efficient similarity search
- **NumPy**: Numerical operations

## Local Development

```bash
# Clone the repository
git clone https://github.com/quinfer/rag-lite-app.git

# Create and activate virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

## Project Structure
```
.
├── README.md
├── requirements.txt
├── app.py                    # Main application entry point
├── project/
│   ├── __init__.py
│   └── app.py               # Core application logic
└── tutorial/
    └── sample_docs/         # Sample PDF documents
        ├── financial_report.pdf
        └── trading_document.pdf
```

## Contributing
We welcome contributions! Feel free to:
- Open issues for bugs or feature requests
- Submit pull requests
- Fork the repository
- Suggest improvements
- Report incorrect answers through the flag feature

## Educational Use
This app is designed for educational purposes:
- Students can quickly find relevant information in course materials
- Researchers can efficiently extract information from papers
- Teachers can monitor common questions through the flagging system
- Continuous improvement based on user feedback

## License
MIT License - feel free to use and modify for your own projects.

## Acknowledgments
- Built as part of the RAG systems educational initiative
- Sample documents created for demonstration purposes
- Community contributions and feedback welcome

## Contact
For questions or suggestions:
- Open an issue on GitHub
- Use the flagging feature in the app

