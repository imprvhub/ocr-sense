from flask import Flask, render_template, request, redirect
import pytesseract
from PIL import Image
import os
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
        image = Image.open(file)
        text = ocr_with_tesseract(image)
        detected_texts.append({'paragraphs': [text]})

    return render_template('result.html', detected_texts=detected_texts)

@app.route('/user_agreements')
def user_agreements():
    return render_template('user_agreements.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
