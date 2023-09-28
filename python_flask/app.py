from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import os

app = Flask(__name__)

url = "https://raw.githubusercontent.com/johncduran/datasci_4_web_viz/main/datasets/PLACES__Local_Data_for_Better_Health__County_Data_2023_release.csv"
df = pd.read_csv(url)


df = df[(df['MeasureId'] == 'DEPRESSION') & (df['Data_Value_Type'] == 'Age-adjusted prevalence')]

grouped = df.groupby('LocationName').Data_Value.mean().sort_values(ascending=False)

# Create an empty file if it does not exist
if not os.path.exists("depression_per_location.png"):
    with open("depression_per_location.png", "wb") as f:
        f.write(b"")

# Save the plot to the file
plt.figure(figsize=(10, 7))
grouped.plot(kind='bar', color='lightcoral')
plt.ylabel('Average Data Value (Age-adjusted prevalence) - Percent')
plt.xlabel('Location (County)')
plt.title('Depression Age-adjusted Prevalence by County in HI')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("depression_per_location.png")

@app.route('/')
def mainpage():
    # Serve the image file to the user
    with open("depression_per_location.png", "rb") as f:
        image = f.read()
    return render_template('base.html', image=image)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=8080,
        host='0.0.0.0'
)