from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def mainpage():
    csv = pd.read_csv('https://raw.githubusercontent.com/johncduran/datasci_4_web_viz/main/datasets/PLACES__Local_Data_for_Better_Health__County_Data_2023_release.csv')
    return render_template('base.html',csv=csv)


if __name__ == '__main__':
    app.run(
        debug=True,
        port=8000
    )