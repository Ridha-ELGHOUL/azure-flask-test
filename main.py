from flask import Flask
from flask import request
from flask import jsonify
from googletrans import Translator
app = Flask(__name__)
def translation(text, target):
    translator = Translator()
    trans= str(translator.translate(text, target))
    transText = trans.split(",")
    return transText[2][6:]

@app.route("/")
def hello():
    return " From Azure Test - TRANS-ATN-Project!"

@app.route('/msgTranslator', methods=['POST'])
def post():
    res=jsonify({'data':''})
    if(request.is_json):
        content = request.get_json()
        ret = translation(content['message'], content['target'])
        print ("Origin data : "+ content['message']+ "  ***** ||*****  Translated Data : "+ ret)
        res = jsonify({'data': str(ret)})
    return res
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
