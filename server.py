from flask import Flask, render_template, request
from nn import *
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        data = request.json
        data = data['arr']
        inputs = (np.asfarray(data[0:]) / 255.0 * 0.99) + 0.01
        outputs = nn.query(inputs)
        nnAnswer = np.argmax(outputs)
        print(nnAnswer)
        return str(nnAnswer)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)