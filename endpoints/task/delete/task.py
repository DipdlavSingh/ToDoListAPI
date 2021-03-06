import copy

from database_models.sql_alchemy_setup import session

from database_models.models.tasks import Task
from database_models.models.lists import List

from helper.update_checker import check_and_update_list_status

import config.constants as constants

def delete_task(task_id, user):
    try:
        task = session.query(Task).filter_by(id = task_id).first()
        if task is None:
            raise Exception('Task does not exist')
        if task:
            _list = session.query(List).filter_by(id = task.listId).first()
            if not _list.user == user['email']:
                raise Exception('Task does not exist')
        res = session.query(Task).filter_by(id = task_id).delete()
        session.commit()
        check_and_update_list_status(task.listId)
        response = copy.deepcopy(constants.SUCCESS_RESPONSE)
        response['data'] = task.as_dict()
        return response
    except Exception as e:
        response = copy.deepcopy(constants.FAIL_RESPONSE)
        response['message'] = str(e)
        return response
