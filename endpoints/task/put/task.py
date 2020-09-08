from database_models.sql_alchemy_setup import session

from database_models.models.tasks import Task

from endpoints.list.get.list import get_list

from helper.update_checker import check_and_update_list_status

import config.constants as constants

def put_task(task_id):
    try:
        task = session.query(Task).filter_by(id = task_id).first()
        if task is None:
            raise Exception('Task does not exist')
        task.completed = not task.completed
        session.commit()

        check_and_update_list_status(task.listId)

        response = constants.SUCCESS_RESPONSE
        response['data'] = get_list(task.listId)['data']
        return response
    except Exception as e:
        response = constants.FAIL_RESPONSE
        response['message'] = str(e)
        return response
