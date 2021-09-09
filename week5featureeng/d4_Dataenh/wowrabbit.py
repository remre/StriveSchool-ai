import heartattacks as sss
import numpy as np
from PIL import Image
import streamlit as st


st.title('Heart Attack Predicter')
st.subheader('This page has a strong Heart attack prediction model background')
img = Image.open("C:/Users/emrre/Downloads/healthy.png")
st.image(img, width=400, use_column_width=True)
st.write("Whis video is simply shows how to use that webapp")
video1 = open("C:/Users/emrre/Downloads/STREAMLITHEART.avi",'rb') 
video_bytes = video1.read()
st.video(video_bytes)
#st.video(video1, start_time = 25)
st.write("Give us answer that we need")




def cli_prediction(age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall):
    model_name =[]
    scores=[]
    for i,modell in enumerate(sss.pipelines):
        pred_arr=np.array([age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall])
        pred_new=pred_arr.reshape(1,-1)
        predik = modell.predict(pred_new)
#cli_model.predict(pred_new)
    return predik


age=st.text_input("Age")
sex=st.text_input("Sex,[0,1]")
cp=st.text_input("cp,[1,3]")
trtbps=st.text_input("trtbps")
chol=st.text_input("chol")
fbs=st.text_input("fbs,[0,1]")
restecg=st.text_input("restecg,[0,2]")
thalachh=st.text_input("thalachh")
exng=st.text_input("exng,[0,1]")
oldpeak=st.text_input("oldpeak") 
slp=st.text_input("slp,[0,2]")
caa=st.text_input("caa,[0,3]") 
thall=st.text_input("thall,[1,3]")



prediction=str('')
if st.button("Predict"):
    prediction=cli_prediction(age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall)
st.success("Result is: {} and her is the guide ==>-0- means you will live -1- means you need a treatment better to visit a doctor".format( prediction )) 


#py -m streamlit run wowrabbit.py