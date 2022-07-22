import streamlit as st 
from PIL import Image
from image_processing import e2e
import cv2

if __name__=='__main__':
    st.title("License Plate Recognition")


    file = st.file_uploader("Upload your image")

    if file:
        img = Image.open(file)
        st.title("Here is the image you have uploaded")
        img.thumbnail((600,500), Image.ANTIALIAS)
        st.image(img)
