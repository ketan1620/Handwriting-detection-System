from flask import Flask, render_template, request
import pytesseract
import cv2
import os
from PIL import Image

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Set Tesseract path (update this path if needed)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

@app.route('/', methods=['GET', 'POST'])
def index():
    extracted_text = ''
    image_path = ''
    if request.method == 'POST':
        if 'image' in request.files:
            img = request.files['image']
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], img.filename)
            img.save(image_path)
            image = cv2.imread(image_path)
            extracted_text = pytesseract.image_to_string(image)
    return render_template('index.html', text=extracted_text, image_path=image_path)

if __name__ == '__main__':
    app.run(debug=True)
    
