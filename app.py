import os
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image
import cv2
from keras.models import load_model
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename


app = Flask(__name__)

#load the best model
model =load_model('final_model_brain_tumor.h5')


def get_classes(classes):
	if classes==0:
		return "No Brain Tumor"
	elif classes==1:
		return "Brain Tumor"

#pre-process the input image and make the prediction
def get_Result(img): 
    image = cv2.imread(img)
    image = Image.fromarray(image, 'RGB')
    image = image.resize((64, 64))
    image = np.array(image)
    input_img = np.expand_dims(image, axis=0)
    result = model.predict(input_img)
    print(f'Model prediction: {result}')
    return result


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

#user upload
@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']

        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        value=get_Result(file_path)
        result=get_classes(value) 
        return result
    return None


if __name__ == '__main__':
    app.run(host='localhost',port=5000,debug=True)