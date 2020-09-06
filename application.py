from flask import Flask, request
import json
import os

from endpoints.all_lists.get.all_lists import get_all_lists

from endpoints.list.get.list import get_list
from endpoints.list.post.list import post_list

from endpoints.task.post.task import post_task

app = Flask(__name__)

@app.route('/allLists', methods = ['GET'])
def __get_lists():
    lists = get_all_lists()
    return json.dumps(lists)

@app.route('/list', methods = ['GET'])
def __get_list():
    list_id = request.get_json().get('listId', None)
    _list = get_list(list_id)
    return json.dumps(_list)

@app.route('/list', methods = ['POST'])
def __post_list():
    event = request.get_json()
    res = post_list(event)
    return json.dumps(res)

@app.route('/task', methods = ['POST'])
def __post_task():
    event = request.get_json()
    res = post_task(event)
    return json.dumps(res)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', debug=True, port = port)
