from database_models.sql_alchemy_setup import session

from database_models.models.tasks import Task
from database_models.models.lists import List

import config.constants as constants

def post_task(event):
    try:
        list_id = event.get("listId", None)
        date_time = event.get("dateTime", None)
        title = event.get("title", None)

        if list_id is None or list_id == '':
            raise Exception('Missing field listId')

        _list = session.query(List).filter_by(id = list_id).first()
        if _list is None:
            raise Exception('List does not exist')        
        
        if title is None or title == '':
            raise Exception('Task title cannot be empty')
        new_task = Task(title = title, listId = list_id, datetime = date_time)
        
        session.add(new_task)
        session.commit()

        response = constants.SUCCESS_RESPONSE
        response['data'] = []
        return response
    except Exception as e:
        response = constants.FAIL_RESPONSE
        response['message'] = str(e)
        return response
