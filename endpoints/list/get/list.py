from database_models.sql_alchemy_setup import session

from database_models.models.tasks import Task
from database_models.models.lists import List

import config.constants as constants

def get_list(list_id):
    try:
        _list = session.query(List).filter_by(id = list_id).first()
        if _list is None:
            raise Exception('List does not exist')
        tasks = session.query(Task).filter_by(listId = list_id).all()
        response = constants.SUCCESS_RESPONSE
        response['data'] = []
        for task in tasks:
            response['data'].append(task.as_dict())
        return response
    except Exception as e:
        response = constants.FAIL_RESPONSE
        response['message'] = str(e)
        return response
