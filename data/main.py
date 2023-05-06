from flask import Flask
import pandas as pd

df = pd.read_csv('./data/data.csv')

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return 'this is an API service for MN ICD code details'

if __name__ == '__main__':
    app.run(debug=True)

    