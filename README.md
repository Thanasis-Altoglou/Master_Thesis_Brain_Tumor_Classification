# Master Thesis Title: Brain Tumor Binary Classification from MRI images using Convolutional Neural Network and VGG16 with Transfer Learning

Brain tumor is the abnormal mass in the cells form within the brain. Precise and accurate brain tumor detection in MRI images plays crucial role in clinical diagnosis and decision making for the treatment of the patients. Applying classical machine learning methods is a very challenging task for a non-expert because it is very time-consuming and prone to errors process. Recent advancement in deep learning has shown huge progress in healthcare, and convolutional neural networks displayed substantial results in image classification tasks.




## Aims:
The aim of this project is to accurately detect and classify brain tumor from MRI images using Convolutional Neural Networks and a pre-trained model named VGG16 with transfer learning. Also, a web application is created as a final data product which predicts whether a brain MRI image is affected by tumor or not. The app is expected to be installed locally by the end-users and it can be used as a diagnostic tool by clinical doctors to make more accurate and faster decisions.

## Research Approach:
The first research approach that will be used in this project for brain tumor prediction is to design and train a Convolutional Neural Network from the scratch, starting from a baseline model and try to improve it through experimentation. Secondly, a pre-trained model called VGG16 will be used, applying the technique of transfer learning.

## Objectives:
At the end of the project, there are several topics which will be clarified and objectives to be met through the literature review and the practical work. These are as follows;
- The impact of Computer Vision and Deep Learning applications on the healthcare, especially in accurately detecting tumor in the brain.
- The main idea behind how convolutional neural networks work to ‘understand’ a brain image well-enough to determine whether a patient has brain tumor.
- Extract and load the dataset found on Kaggle and perform pre-processing steps to prepare the data for training.
- Build and train the deep learning models to accurately detect tumor in brain MRI images using TensorFlow framework and keras library.
- How to prevent the challenge of overfitting during the training phase of the models.
- Evaluate and compare the performance of the final Convolution Neural Network and the VGG16 model using various evaluation metrics such as the learning curves, accuracy, and confusion matrices choosing the best model to deploy in the web application.
- Develop the front-end of the website using HTML, CSS, and Bootstrap as well as the back-end using Flask framework and Python programming language.

## Results:
- Approach 1:
The image below  displays the learning curves of the final model created from the scratch. The model performed very well achieving 98% overall accuracy in brain tumor classification.
![image](https://user-images.githubusercontent.com/102918064/196651444-2b5de070-cde0-4afd-8646-b5cdd529dd99.png)

- Approach 2:
The performance of the pre-trained model can be seen in the next figure. The pre-trained model obtained 91% accuracy for brain tumor detection.

![image](https://user-images.githubusercontent.com/102918064/196654774-cbbc5705-2e9a-463a-95aa-90141e752d65.png)


## Front-end of the application:
![Screenshot (165)](https://user-images.githubusercontent.com/102918064/202382406-5f7c2baf-8397-4913-a08a-23e435d93308.png)

# Results:

![Screenshot (171)](https://user-images.githubusercontent.com/102918064/202382504-2417c6e5-7012-4635-bb6b-445784056743.png)

![Screenshot (173)](https://user-images.githubusercontent.com/102918064/202382525-c49ac81d-1d23-4f11-81dd-5ffb43f04111.png)




## About the dataset.
A publicly available dataset is used in this research which is found in [Kaggle](https://www.kaggle.com/datasets/ahmedhamada0/brain-tumor-detection). This dataset consists of three folders. A folder called ‘no’ which contains 1500 brain MRI images that are not affected by tumor, a ‘yes’ folder with 1500 MRI images which are tumorous, and a ‘pred’ folder with 60 brain MRI images to make final predictions.
