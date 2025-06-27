import streamlit as st
import leafmap.foliumap as leafmap
from PIL import Image


#Establecer configuracion de la pagina
st.set_page_config(layout="centered")

#Se establece el encabezado
st.header("Ejemplo basico de la creacion de un dashboard")

st.title("Aquí los alumnos aprenderan a hacer un pequeño dashboard")


#Para colocacr una imagen lo hacemos de la siguiente manera
st.markdown("Esto es un ejemplo de una imagen")
st.image("Imagen_Resultados.jpg")


#Ejemplo para subir archivos a la pagina 
st.markdown("Ejemplo de como subir archivos a la página")
file_uploader = st.file_uploader("Sube alguna imagen",type=["jpg","png"])

if file_uploader is not None:
        image = Image.open(file_uploader)
        st.image(image)


#Ejemplo de como tener un mapa en la aplicación
st.markdown("Mapa de leaflet")
m = leafmap.Map(center=[25.67, -100.31847], zoom=7, minimap_control=True)
m.to_streamlit(height=800)

st.markdown("Mapa de Google")
m2 = leafmap.Map(google_map="HYBRID", center=[25.67, -100.31847], zoom=7, minimap_control=True)
m2.to_streamlit(height=800)

#streamlit run Tutorial_basico.py --server.port 8888