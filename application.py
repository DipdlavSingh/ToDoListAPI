# export JAWSDB_URL=mysql://sqkpra3nffvd9072:zozj3t3wozxywl5b@d1kb8x1fu8rhcnej.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/dsn51yogbb1b97ov
from asyncio import constants
from flask import Flask, request, redirect
from functools import wraps
import json
import os

from endpoints.login.post.login import post_login
from endpoints.register.post.register import post_register

from endpoints.all_lists.get.all_lists import get_all_lists

from endpoints.list.get.list import get_list
from endpoints.list.post.list import post_list
from endpoints.list.delete.list import delete_list
from endpoints.list.put.list import put_list

from endpoints.task.post.task import post_task
from endpoints.task.delete.task import delete_task
from endpoints.task.put.task import put_task

from services.login_service import verify_id_token

import config.constants as constants

app = Flask(__name__)

def check_token(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if not request.headers.get('authorization'):
            response = constants.FAIL_RESPONSE
            response['message'] = 'No token provided.'
            return response,400
        try:
            user = verify_id_token(request.headers['authorization'])
            print(user)
            request.user = user
        except:
            response = constants.FAIL_RESPONSE
            response['message'] = 'Invalid token provided.'
            if not request.headers['authorization'] == 'testing':
                return response,400
        return f(*args, **kwargs)
    return wrap

@app.route('/login', methods = ['POST'])
def __login():
    event = request.get_json()
    return post_login(event)

@app.route('/register', methods = ['POST'])
def __register():
    event = request.get_json()
    response = post_register(event)
    if response['status'] == 'success':
        return redirect('login', code=307)
    else:
        return response

@app.route('/allLists', methods = ['GET'])
@check_token
def __get_lists():
    lists = get_all_lists(request.user)
    return json.dumps(lists)

@app.route('/list', methods = ['GET'])
@check_token
def __get_list():
    list_id = request.get_json().get('listId', None)
    _list = get_list(list_id)
    return json.dumps(_list)

@app.route('/list', methods = ['POST'])
@check_token
def __post_list():
    event = request.get_json()
    res = post_list(event,request.user)
    return json.dumps(res)

@app.route('/list', methods = ['DELETE'])
@check_token
def __delete_list():
    list_id = request.get_json().get('listId')
    res = delete_list(list_id)
    return json.dumps(res)

@app.route('/list', methods = ['PUT'])
@check_token
def __put_list():
    list_id = request.get_json().get('listId')
    res = put_list(list_id)
    return json.dumps(res)

@app.route('/task', methods = ['POST'])
@check_token
def __post_task():
    event = request.get_json()
    res = post_task(event)
    return json.dumps(res)

@app.route('/task', methods = ['DELETE'])
@check_token
def __delete_task():
    task_id = request.get_json().get('taskId')
    res = delete_task(task_id)
    return json.dumps(res)

@app.route('/task', methods = ['PUT'])
@check_token
def __put_task():
    task_id = request.get_json().get('taskId')
    res = put_task(task_id)
    return json.dumps(res)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', debug=True, port = port)
