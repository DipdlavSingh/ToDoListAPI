from flask import Flask, request
import json
import os

from endpoints.all_lists.get.all_lists import get_all_lists

from endpoints.tasks.get.tasks import get_tasks

app = Flask(__name__)

@app.route('/allLists', methods = ['GET'])
def get_lists():
    lists = get_all_lists()
    return json.dumps(lists)

@app.route('/list', methods = ['GET'])
def get_list():
    list_id = request.get_json().get('listId', None)
    tasks = get_tasks(list_id)
    return json.dumps(tasks)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', debug=True, port = port)
