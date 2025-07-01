import PyPDF2
import docx2txt

def extract_text(file):
    if file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        return "".join([page.extract_text() or "" for page in reader.pages])
    elif file.name.endswith(".docx"):
        return docx2txt.process(file)
    else:
        return ""

def extract_multiple_resumes(files):
    return {file.name: extract_text(file) for file in files}