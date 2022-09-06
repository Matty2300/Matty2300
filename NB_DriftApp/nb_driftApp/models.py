from email.policy import default
from importlib.metadata import metadata
from sqlalchemy import column, create_engine,Column,DateTime,Integer,String,Text, DATE, ForeignKey
from sqlalchemy.orm import relationship
from nb_driftApp import login_manager
from datetime import datetime
from flask_login import UserMixin
from nb_driftApp.database import Base




#session managing
@login_manager.user_loader
def load_user(user_id):# user_id as argument
    return User.query.get(int(user_id)) #getting user by ID , creating a session ID

class User(Base, UserMixin):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key = True)
    email = Column(String, unique=True)
    fornavn = Column(String)
    efternavn = Column(String)
    username = Column(String)
    password = Column(String)
    
    def __init__(self, email=None, password=None, fornavn=None, efternavn=None, username=None):
        self.email = email
        self.password = password
        self.fornavn = fornavn
        self.efternavn = efternavn
        self.username = username
    
    def __repr__(self):
        return f"User('{self.email}')"
    

    
class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key = True)
    headline = Column(String)
    date_posted = Column(DateTime, default=datetime.utcnow)
    msg_content = Column(Text)
    author = Column(String)
    expiration_date = Column(DATE)
    
    @property
    def formatted_expiration_date(self):
        return self.expiration_date.strftime("%D/%m/%Y")
    
    def __init__(self, headline=None, date_posted=None, msg_content=None, author=None, expiration_date=None):
        self.headline = headline
        self.date_posted = date_posted
        self.msg_content = msg_content
        self.expiration_date = expiration_date
        self.author = author
        
    def __repr__(self):
        return f"Post('{self.author}{self.headline}{self.date_posted}')"