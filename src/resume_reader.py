import pdfplumber

def read_resume(file):

    if file.filename.endswith(".txt"):
        return file.read().decode("utf-8")

    elif file.filename.endswith(".pdf"):

        text = ""

        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        return text

    else:
        return ""