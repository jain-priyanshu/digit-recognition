from tensorNN import tensorNNPredict
from flask import Flask, render_template, request
from nn import *

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        #loading wegihts with pickle
        file = 'weights.txt'
        t = pickle.load(open(file, 'rb'))
        wih = t[0]
        who = t[1]

        #changing weights manually
        nn.changeWeights(wih, who)

        data = request.json
        data = data['arr']
        inputs = (np.asfarray(data[0:]) / 255.0 * 0.99) + 0.01
        outputs = nn.query(inputs)
        nnAnswer = np.argmax(outputs)
        print("My NN: ", nnAnswer)
        tensorNN = tensorNNPredict(inputs)
        print("Tensor NN: ", tensorNN)

        return {1: int(nnAnswer), 2: int(tensorNN)}
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)