from flask import Flask, render_template
import requests

app = Flask(__name__)

def data_indo():
    url = 'https://api.kawalcorona.com/indonesia/'
    getData = requests.get(url).json()
    return getData


@app.route('/')
def indo_data():
   return render_template('index.html', data_indo=data_indo())

if __name__ == '__main__':
    app.run(debug=True)