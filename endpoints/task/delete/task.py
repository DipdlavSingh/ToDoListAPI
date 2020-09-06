from database_models.sql_alchemy_setup import session

from database_models.models.tasks import Task

import config.constants as constants

def delete_task(task_id):
    try:
        _list = session.query(Task).filter_by(id = task_id).first()
        if _list is None:
            raise Exception('Task does not exist')
        res = session.query(Task).filter_by(id = task_id).delete()
        session.commit()
        response = constants.SUCCESS_RESPONSE
        response['data'] = _list.as_dict()
        return response
    except Exception as e:
        response = constants.FAIL_RESPONSE
        response['message'] = str(e)
        return response
