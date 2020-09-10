from database_models.sql_alchemy_setup import session

from database_models.models.tasks import Task
from database_models.models.lists import List

from endpoints.all_lists.get.all_lists import get_all_lists

from helper.update_checker import check_and_update_list_status, update_tasks_status

import config.constants as constants

def put_list(list_id, user):
    try:
        list = session.query(List).filter_by(id = list_id).filter_by(user = user['email']).first()
        if list is None:
            raise Exception('List does not exist')
        
        if list.completed:
            list.completed = False
        else:
            list.completed = True
        session.commit()

        update_tasks_status(list_id, list.completed)

        response = constants.SUCCESS_RESPONSE
        response['data'] = get_all_lists(user)['data']
        return response
    except Exception as e:
        response = constants.FAIL_RESPONSE
        response['message'] = str(e)
        return response
