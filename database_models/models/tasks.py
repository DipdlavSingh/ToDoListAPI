from datetime import datetime
from database_models.sql_alchemy_setup import session, Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

class Task(Base):
     __tablename__ = 'tasks'

     id = Column(Integer, autoincrement = True, primary_key=True)
     title = Column(String(255), nullable = False)
     datetime = Column(DateTime, nullable = True)
     listId = Column(Integer, ForeignKey('lists.id'))
     completed = Column(Integer, nullable = False)

     def as_dict(self):
          return {
               'id': self.id,
               'title': self.title,
               'datetime': self.datetime,
               'listId': self.listId,
               'completed': self.completed
          }
