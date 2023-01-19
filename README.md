# ¿Para qué sirve este dado?
<b>Author: Almudena Ramírez</b>

Este proyecto se basa en una red neuronal entrenada para distinguir distintos tipos de dados empleados en juegos de rol. Estos dados se clasifican según el número de caras que presentan (4, 6, 8, 10, 12 o 20). 
 

## Dataset
El dataset empleado para este proyecto se puede descargar en https://www.kaggle.com/datasets/ucffool/dice-d4-d6-d8-d10-d12-d20-images.
Características:
* Las imágenes ya vienen separadas en train y test
* Las imágenes vienen en distintos fondos, colores, orientaciones y ángulos
* Las imágenes están clasificadas en subcarpetas en función de su número de caras
* La mayoría son 480x480


## Elementos del proyecto
Este repositorio se compone principalmente de:
* Una carpeta con el dataset (dice-d4-d6-d8-d10-d12-d20) dividido en distintas subcarpetas
* Archivo 'entrenamiento.py' con el entrenamiento de la red neuronal utilizando Mobilenet
* Modelo entrenado (modelo.h5)
* Archivo 'predicción.py' donde se ejecuta la predicción de los archivos que le vamos a dar
* Archivo 'main.py' en el que está la organización del dashboard en streamlit

## Cómo se ejecuta el proyecto
En el documento "requirements.txt" están los programas y sus versiones utilizados para crear el proyecto.

### Ejecutar streamlit
En el terminal, ejecutar el fichero `streamlit_main.py`

```bash
streamlit run 'streamlit_main.py'
```
