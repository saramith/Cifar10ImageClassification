from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from src.evaluate import evaluate_model
from src.predict import predict_image

application = Flask(__name__)

app=application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/evaluate')
def evaluate_route():
    # Call the evaluate function
    result = evaluate_model()
    return f"Evaluate function called with result: {result}"

@app.route('/predict', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file'
    
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join('upload_folder', filename)
        file.save(file_path)
        # Call predict_image function with the uploaded image path
        result = predict_image(file_path)
        return render_template('index.html', prediction_result=result)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
