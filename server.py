
from flask import Flask, request, jsonify
from emotion_detector import emotion_detector

app = Flask(__name__)

@app.route('/emotion', methods=['POST'])
def analyze_emotion():
    text_to_analyze = request.get_json()['text']
    result = emotion_detector(text_to_analyze)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

