import pdfplumber

def extract_resume_text(pdf_file):
    """Extract clean text from PDF resume."""
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text
