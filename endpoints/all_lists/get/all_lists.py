import copy

from database_models.sql_alchemy_setup import session

from database_models.models.lists import List

import config.constants as constants

def get_all_lists():
    try:
        session.commit()
        lists = session.query(List).all()
        response = copy.deepcopy(constants.SUCCESS_RESPONSE)
        response['data'] = []
        for list in lists:
            response['data'].append(list.as_dict())
        return response
    except Exception as e:
        response = constants.FAIL_RESPONSE
        response['message'] = str(e)
        return response
