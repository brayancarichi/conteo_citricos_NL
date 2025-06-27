import streamlit as st
from ultralytics import YOLO
from ultralytics.solutions import object_counter


import imutils
import os
from os import mkdir
from datetime import date
from datetime import datetime
from getpass import getuser
import supervision as sv
from PIL import Image

import matplotlib.path as mplPath
import matplotlib.pyplot as plt



from PIL import Image

from ultralytics import YOLO
from ultralytics.solutions import object_counter


import matplotlib.path as mplPath
import matplotlib.pyplot as plt
import imutils
import gdown
from functions import *


def main():
    
    st.header('Aplicación para el conteo de cítricos ')
    st.markdown('Aplicación desarrollada por Brayan Murillo Gutiérrez. Detecta los cítricos que se encuentran en el árbol a partir de una imagen. Se muestran dos resultados: M = fruta madura   MN = fruta que aun no esta madura y presenta tonalidades verdosas. ')

    file_uploader = st.file_uploader('Sube tu imagen en los siguientes formatos: ', type=['jpg', 'png'])

    if file_uploader is not None:
        image = Image.open(file_uploader)
        print(image)
        

        st.image(image)
        datos = deteccion(image)
        st.markdown('Los resultados de la imagen de salida fueron modificados con el fin de que sea más fácil para la red neuronal hacer las detecciones de las frutas.')
        st.image(deteccion((image)))

        st.markdown(deteccion2((image)) + ' Cítricos detectados')

        


if __name__ == "__main__":
    main()




#streamlit run Principal.py --server.port 8888
#streamlit run .\Dash.py --server.port 8888