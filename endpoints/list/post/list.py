import copy

from database_models.sql_alchemy_setup import session

from database_models.models.lists import List

import config.constants as constants

def post_list(event, user):
    try:
        title = event.get('title', None)
        user = user['email']

        if title is None or title == '':
            raise Exception("Title cannot be Null")
        new_list = List(title = title, user = user)
        session.add(new_list)
        session.commit()
        response = copy.deepcopy(constants.SUCCESS_RESPONSE)
        response['data'] = None
        return response
    except Exception as e:
        response = copy.deepcopy(constants.FAIL_RESPONSE)
        response['message'] = str(e)
        return response
