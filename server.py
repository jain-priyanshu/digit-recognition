from flask import Flask, render_template, request
from nn import *
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        x = request.json
        y = sumArr(x)
        print("HERE: ")
        print(y)
        return request.json
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)