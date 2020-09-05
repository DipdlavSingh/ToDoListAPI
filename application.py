from flask import Flask
import json
import os

app = Flask(__name__)

@app.route('/allLists', methods = ['GET'])
def get_lists():
    dummy_lists = [{'title':'list 1', 'completed': True}]
    return json.dumps(dummy_lists)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', debug=True, port = port)
