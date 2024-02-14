from flask import Flask, render_template, request, redirect
import pytesseract
from PIL import Image
import os
import PyPDF2
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('PRODUCTION_KEY')

def ocr_with_tesseract(image):
    text = pytesseract.image_to_string(image)
    return text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return redirect(request.url)

    files = request.files.getlist('image')
    detected_texts = []

    for file in files:
        if file.filename == '':
            continue
        if file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image = Image.open(file)
            text = ocr_with_tesseract(image)
            detected_texts.append({'paragraphs': [text]})
        elif file.filename.lower().endswith('.pdf'):
            text = ocr_pdf(file)
            detected_texts.append({'paragraphs': [text]})
        else:
            continue

    return render_template('result.html', detected_texts=detected_texts)

def ocr_pdf(file):
    pdf_text = ''
    reader = PyPDF2.PdfReader(file)
    num_pages = len(reader.pages)
    for page_num in range(num_pages):
        page = reader.pages[page_num]
        pdf_text += page.extract_text()
    return pdf_text

@app.route('/user_agreements')
def user_agreements():
    return render_template('user_agreements.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
