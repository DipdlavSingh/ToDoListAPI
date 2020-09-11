import copy

from database_models.sql_alchemy_setup import session

from database_models.models.tasks import Task
from database_models.models.lists import List

import config.constants as constants

def get_list(list_id, user):
    try:
        _list = session.query(List).filter_by(id = list_id).filter_by(user=user['email']).first()
        if _list is None:
            raise Exception('List does not exist')
        session.commit()
        tasks = session.query(Task).filter_by(listId = list_id).all()
        response = copy.deepcopy(constants.SUCCESS_RESPONSE)
        response['data'] = []
        for task in tasks:
            response['data'].append(task.as_dict())
        return response
    except Exception as e:
        response = copy.deepcopy(constants.FAIL_RESPONSE)
        response['message'] = str(e)
        return response
