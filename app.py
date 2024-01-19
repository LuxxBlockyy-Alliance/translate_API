from flask import Flask, request, jsonify
from googletrans import Translator


app = Flask(__name__)
translator = Translator()

@app.route('/translate', methods=['POST'])
def translate_text():
    text = request.json['text']
    translation = translator.translate(text, dest='de')
    translated_text = translation.text
    return jsonify({'translated_text': translated_text})


if __name__ == '__main__':
    app.run(debug=True, host="	172.17.0.6")