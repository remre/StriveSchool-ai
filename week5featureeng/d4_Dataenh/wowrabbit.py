{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "wowrabbit.py",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyOJay/TuuPOU3NScfugQ5kY",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/remre/StriveSchool-ai/blob/main/week5featureeng/d4_Dataenh/wowrabbit.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "lFxtKyCMtKlb"
      },
      "source": [
        "import heartattacks as sss\n",
        "import numpy as np\n",
        "from PIL import Image\n",
        "import streamlit as st\n",
        "\n",
        "\n",
        "st.title('Heart Attack Predicter')\n",
        "st.subheader('This page has a strong Heart attack prediction model background')\n",
        "img = Image.open(\"C:/Users/emrre/Downloads/healthy.png\")\n",
        "st.image(img, width=400, use_column_width=True)\n",
        "st.write(\"Whis video is simply shows how to use that webapp\")\n",
        "video1 = open(\"C:/Users/emrre/Downloads/STREAMLITHEART.avi\",'rb') \n",
        "video_bytes = video1.read()\n",
        "st.video(video_bytes)\n",
        "#st.video(video1, start_time = 25)\n",
        "st.write(\"Give us answer that we need\")\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "def cli_prediction(age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall):\n",
        "    model_name =[]\n",
        "    scores=[]\n",
        "    for i,modell in enumerate(sss.pipelines):\n",
        "        pred_arr=np.array([age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall])\n",
        "        pred_new=pred_arr.reshape(1,-1)\n",
        "        predik = modell.predict(pred_new)\n",
        "#cli_model.predict(pred_new)\n",
        "    return predik\n",
        "\n",
        "\n",
        "age=st.text_input(\"Age\")\n",
        "sex=st.text_input(\"Sex,[0,1]\")\n",
        "cp=st.text_input(\"cp,[1,3]\")\n",
        "trtbps=st.text_input(\"trtbps\")\n",
        "chol=st.text_input(\"chol\")\n",
        "fbs=st.text_input(\"fbs,[0,1]\")\n",
        "restecg=st.text_input(\"restecg,[0,2]\")\n",
        "thalachh=st.text_input(\"thalachh\")\n",
        "exng=st.text_input(\"exng,[0,1]\")\n",
        "oldpeak=st.text_input(\"oldpeak\") \n",
        "slp=st.text_input(\"slp,[0,2]\")\n",
        "caa=st.text_input(\"caa,[0,3]\") \n",
        "thall=st.text_input(\"thall,[1,3]\")\n",
        "\n",
        "\n",
        "\n",
        "prediction=str('')\n",
        "if st.button(\"Predict\"):\n",
        "    prediction=cli_prediction(age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall)\n",
        "st.success(\"Result is: {} and her is the guide ==>-0- means you will live -1- means you need a treatment better to visit a doctor\".format( prediction )) \n",
        "\n",
        "\n",
        "#py -m streamlit run wowrabbit.py"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}