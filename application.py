# export JAWSDB_URL=mysql://sqkpra3nffvd9072:zozj3t3wozxywl5b@d1kb8x1fu8rhcnej.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/dsn51yogbb1b97ov
from flask import Flask, request
import json
import os

from endpoints.all_lists.get.all_lists import get_all_lists

from endpoints.list.get.list import get_list
from endpoints.list.post.list import post_list
from endpoints.list.delete.list import delete_list
from endpoints.list.put.list import put_list

from endpoints.task.post.task import post_task
from endpoints.task.delete.task import delete_task
from endpoints.task.put.task import put_task

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

@app.route('/list', methods = ['DELETE'])
def __delete_list():
    list_id = request.get_json().get('listId')
    res = delete_list(list_id)
    return json.dumps(res)

@app.route('/list', methods = ['PUT'])
def __put_list():
    list_id = request.get_json().get('listId')
    res = put_list(list_id)
    return json.dumps(res)

@app.route('/task', methods = ['POST'])
def __post_task():
    event = request.get_json()
    res = post_task(event)
    return json.dumps(res)

@app.route('/task', methods = ['DELETE'])
def __delete_task():
    task_id = request.get_json().get('taskId')
    res = delete_task(task_id)
    return json.dumps(res)

@app.route('/task', methods = ['PUT'])
def __put_task():
    task_id = request.get_json().get('taskId')
    res = put_task(task_id)
    return json.dumps(res)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', debug=True, port = port)
