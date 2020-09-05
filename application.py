from flask import Flask
import json

app = Flask(__name__)

@app.route('/allLists', methods = ['GET'])
def get_lists():
    dummy_lists = [{'title':'list 1', 'completed': True}]
    return json.dumps(dummy_lists)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
