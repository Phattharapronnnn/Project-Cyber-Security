from flask import Flask, render_template
import json
import os
from getdata import getdata

app = Flask(__name__)

@app.route('/getdata')
def load_data():
    getdata()
    file_path = os.path.join(os.path.dirname(__file__), 'data_all.json')
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data



@app.route('/')
def index():
    
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)