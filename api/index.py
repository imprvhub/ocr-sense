from flask import Flask, render_template, request, redirect
import pytesseract
from PIL import Image
import nltk

nltk.download('punkt')


app = Flask(__name__)

def detect_titles_and_paragraphs(text):
    lines = text.split('\n')
    titles = []
    paragraphs = []

    for line in lines:
        if line.isupper() and line.endswith('.'):
            titles.append(line)
        else:
            paragraphs.append(line)

    return titles, paragraphs


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
        text = pytesseract.image_to_string(image)

        titles, paragraphs = detect_titles_and_paragraphs(text)
        detected_texts.append({'titles': titles, 'paragraphs': paragraphs})

    return render_template('result.html', detected_texts=detected_texts)

@app.route('/user_agreements')
def user_agreements():
    return render_template('user_agreements.html')

if __name__ == '__main__':
    app.run(debug=True)
