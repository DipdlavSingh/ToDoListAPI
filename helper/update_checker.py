from database_models.sql_alchemy_setup import session

from database_models.models.tasks import Task
from database_models.models.lists import List

import config.constants as constants

def check_and_update_list_status(list_id):
    list = session.query(List).filter_by(id = list_id).first()
    tasks = session.query(Task).filter_by(listId = list_id).all()

    for task in tasks:
        if not task.completed:
            list.completed = False
            session.commit()
            return

    list.completed = True
    session.commit()


