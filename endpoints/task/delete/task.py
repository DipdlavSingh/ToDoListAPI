from database_models.sql_alchemy_setup import session

from database_models.models.tasks import Task

from helper.update_checker import check_and_update_list_status

import config.constants as constants

def delete_task(task_id):
    try:
        task = session.query(Task).filter_by(id = task_id).first()
        if task is None:
            raise Exception('Task does not exist')
        res = session.query(Task).filter_by(id = task_id).delete()
        session.commit()
        check_and_update_list_status(task.listId)
        response = constants.SUCCESS_RESPONSE
        response['data'] = task.as_dict()
        return response
    except Exception as e:
        response = constants.FAIL_RESPONSE
        response['message'] = str(e)
        return response
