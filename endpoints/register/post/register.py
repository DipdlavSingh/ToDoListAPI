import copy
from database_models.sql_alchemy_setup import session

import config.constants as constants

from services.login_service import register_user

def post_register(event):
    try:
        email = event.get('email', None)
        password = event.get('password', None)

        if (not email) or (not password):
            raise Exception('No email/password given')

        logged_in, user = register_user(email, password)
        if (not logged_in):
            raise Exception('Could not register')

        response = copy.deepcopy(constants.SUCCESS_RESPONSE)
        response['data'] = None
        # response['token'] = user['idToken']
        return response
    except Exception as e:
        response = copy.deepcopy(constants.FAIL_RESPONSE)
        response['message'] = str(e)
        return response
