import copy

import datetime

from database_models.sql_alchemy_setup import session

from database_models.models.tasks import Task
from database_models.models.lists import List

from helper.update_checker import check_and_update_list_status

import config.constants as constants

def post_task(event, user):
    try:
        list_id = event.get("listId", None)
        date_time_str = event.get("dateTime", None)
        date_time_obj = None
        if date_time_str:
            date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
        title = event.get("title", None)

        if list_id is None or list_id == '':
            raise Exception('Missing field listId')

        _list = session.query(List).filter_by(id = list_id).filter_by(user=user['email']).first()
        if _list is None:
            raise Exception('List does not exist')        
        
        if title is None or title == '':
            raise Exception('Task title cannot be empty')
        new_task = Task(title = title, listId = list_id, datetime = date_time_obj)
        
        session.add(new_task)
        session.commit()

        check_and_update_list_status(list_id)

        response = copy.deepcopy(constants.SUCCESS_RESPONSE)
        response['data'] = []
        return response
    except Exception as e:
        response = copy.deepcopy(constants.FAIL_RESPONSE)
        response['message'] = str(e)
        return response
