import streamlit as st
from PIL import Image
import end2end_recognition as lpr
import cv2



if __name__=='__main__':
    st.title("License Plate Recognition")

    file = st.file_uploader("Upload your image")

    if file:
        img = Image.open(file)
        st.title("Here is the image you have uploaded")
        st.image(img)
        img.save("testing_img/img.jpg")
        st.write("Please wait...")


        img = cv2.imread('testing_img/img.jpg')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        st.subheader('Character-based method')
        st.write(lpr.end2end_character_based(img))

        st.subheader('Segment-based method')
        st.write(lpr.end2end_segment_based(img))
