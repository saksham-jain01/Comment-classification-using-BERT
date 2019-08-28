from flask import Flask
from flask import request
from flask import jsonify

import sys
sys.path.append("./bert")
from bert.run_classifier import ColaProcessor
from prediction import BertPrediction

app = Flask(__name__)

processor = ColaProcessor()
predictor = BertPrediction(processor, "./bert_output")

@app.route('/result',methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    text = data['text']

    # Make prediction using model loaded from disk as per the data.
    result = predictor.run(text)

    # Take the first value of prediction
    output = int(result[0])
    return jsonify(output)

if __name__ == '__main__':
    app.run(port=5000, debug=True)