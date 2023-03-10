import streamlit as st
import cv2
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from PIL import Image
from tensorflow.keras import preprocessing


"""def preprocess_image(im_path):
    im = cv2.imread(im_path, cv2.IMREAD_UNCHANGED)
    if im is None: 
        print("La imagen no se ha leido correctamente: ", im_path)
        return None

    # Escalar los pixeles a un rango de 0 a 1
    # Redimensionar el tamaño de la imagen
    im = cv2.resize(im, (IMG_WIDTH, IM_HEIGHT))
    return im

"""
def predict(im):
    model = model
    test_image = preprocess_image(image)
    test_image = preprocessing.image.img_to_array(test_image)
    test_image = test_image / 255.0
    test_image = np.expand_dims(test_image, axis=0)
    class_names = ['drink' 'food' 'inside' 'menu' 'outside']
    scores = tf.nn.softmax(predictions[0])
    scores = scores.numpy()
    results = {
        'drink': 0,
        'food': 0,
        'inside': 0,
        'menu': 0,
        'outside': 0,
    }
    result = f"{class_names[np.argmax(scores)]} with a {(100 * np.max(scores)).round(2)} percent confidence."
    return result

st.header("What is the category? Yelp edition")
file_uploaded = st.file_uploader("Choose file", type= ['png', 'jpg', 'jpeg'])

if file_uploaded is not None:
    fig, ax = plt.subplots()
    image = Image.open(file_uploaded)
    plt.imshow(image)
    predictions = predict(image)
    st.write(predictions)
    fig = plt.figure()
    st.pyplot(fig)