from database_models.sql_alchemy_setup import session, Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

class List(Base):
     __tablename__ = 'lists'

     id = Column(Integer, autoincrement = True, primary_key=True)
     title = Column(String(255), nullable = False)
     user = Column(String(255), nullable = True)
     completed = Column(Boolean, nullable = False, default = False)

     tasks = relationship('Task', cascade = 'all, delete')

     def as_dict(self):
          return {
               'id': self.id,
               'title': self.title,
               'user': self.user,
               'completed': self.completed
          }
