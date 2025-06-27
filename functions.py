import streamlit as st
from ultralytics import YOLO
from ultralytics.solutions import object_counter

import numpy as np
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

import numpy as np
import matplotlib.path as mplPath
import matplotlib.pyplot as plt
import imutils



import requests
def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)  

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)


def load_model(self):
        cloud_model_location = "1jbDLmw_ZWjDgUlVGrVde4h68U1edPzdT"
        save_dest = Path('model')
        save_dest.mkdir(exist_ok=True)

        f_checkpoint = Path("bestNDVI.pt")

        if not f_checkpoint.exists():
            with st.spinner("Downloading model... this may take awhile! \n Don't stop it!"):
                from GD_download import download_file_from_google_drive
                download_file_from_google_drive(cloud_model_location, f_checkpoint)

        checkpoint = torch.load(f_checkpoint, map_location=device)
        self.net_G.load_state_dict(checkpoint['model_G_state_dict'])
        self.net_G.to(device)
        self.net_G.eval()
        
        
        del f_checkpoint
        del checkpoint
        
          




def deteccion(image):
    
    

    

   
    
    
    model = YOLO("Models25/bestCitricos.pt")
    imagen = image
    result = model(imagen,imgsz = 640, conf = 0.1, show_labels=False,show_conf=False)[0]
    resultados = model.predict(imagen, imgsz = 640, conf = 0.1)
    detections = sv.Detections.from_ultralytics(result)
    alta = detections[detections.confidence > 0.1]
    
    leng = len(resultados)
    
    anotaciones = resultados[0].plot()
    haber = imutils.resize(anotaciones,width=640)
    
    
    haber = imutils.resize(anotaciones,width=1024)
    
    
    
    
    return haber



def deteccion2(image):
    
    model = YOLO("Models25/bestCitricos.pt")
    imagen = image
    result = model(imagen,imgsz = 640, conf = 0.1, show_labels=False,show_conf=False)[0]
    resultados = model.predict(imagen, imgsz = 640, conf = 0.1)
    detections = sv.Detections.from_ultralytics(result)
    alta = detections[detections.confidence > 0.1]
    
    leng = len(resultados)
    
    anotaciones = resultados[0].plot()
    haber = imutils.resize(anotaciones,width=640)
    
    leng = len(alta)
    leng2 = str(leng)
    
    haber = imutils.resize(anotaciones,width=1024)
  
    
    
    return leng2




