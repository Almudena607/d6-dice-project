from keras.models import load_model
from PIL import Image
import numpy as np
import streamlit as st
from urllib.request import urlretrieve

def predict_dice(img_path):
    model = load_model("modelo.h5")
    img = Image.open(img_path)
    img = img.resize((64, 64))
    x = np.array(img)
    x = x / 255
    x = np.expand_dims(x, axis=0)
    preds = model.predict(x)
    class_idx = np.argmax(preds[0])
    class_label = ['d10','d12','d20','d4','d6','d8'][class_idx]
    return class_label

st.markdown("# Clasificación de Dados")
st.image("header.jpg")
st.write("¿Cuando te hablan de dados solo te vienen a la cabeza esos aburridos del parchís? En verdad hay mucha diversidad en cuanto a dados se refiere, cada uno con una función muy específica, especialmente relacionada con el juego de rol y juegos de mesa. Con este proyecto te explicaremos cómo se llaman y para qué sirve cada uno de estos dados con tan solo una imagen.")
st.write("Este proyecto consiste en la predicción del tipo de dado según el número de caras que tenga. Para ello ingresa a continuación una URL o sube un archivo (.jpg o .png) con la imagen de un dado.")

st.markdown("## ¿Para qué sirve este dado?")
img_url = st.text_input("Ingresa la URL de una imagen")
img_path = "temp.jpg"
if img_url:
    urlretrieve(img_url, img_path)
else:
    img_path = st.file_uploader("Subir una imagen", type=["jpg", "png"])

if st.button("Predecir"):
    class_label = predict_dice(img_path)
    st.write("## La imagen pertenece a la clase: ", class_label)
    if class_label == "d4":
        st.write("Una tirada del d4 se utiliza para determinar el daño causado por un arma pequeña.")
    if class_label == "d6":
        st.write("Las tiradas del d6 son lo que constituye la base de la generación de personajes dentro del juego. Los atributos principales de un personaje (Fuerza, Destreza, Constitución, Inteligencia, Sabiduría y Carisma) se basan inicialmente en una tirada de 3 dados 3D6, de modo que cada característica tiene una puntuación de entre 3 y 18.")
    if class_label == "d8":
        st.write("Una tirada del d8 se utiliza para determinar el daño causado por un arma mediana.")
    if class_label == "d10":
        st.write("Una tirada del d10 se utiliza para determinar el daño causado por un arma grande.")
    if class_label == "d12":
        st.write("Una tirada del d12 se utiliza para determinar el daño causado por un arma grande.")
    if class_label == "d20":
        st.write("El dado de 20 caras (d20) se utiliza generalmente para ver si has tenido éxito en una tarea determinada. Tus habilidades (nivel, fuerza, raza, etc.) determinarán la puntuación que necesitas conseguir. Un D20 determina el éxito o el fracaso de ataques, salvación o uso de habilidades.")
