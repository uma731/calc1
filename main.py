
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def result():
    return render_template('index.html', entry=entry)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
