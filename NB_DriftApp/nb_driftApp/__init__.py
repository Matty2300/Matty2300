import urllib
from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_ckeditor import CKEditor
import os
ServerCon = os.getenv('db_connect')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ntRg1sjozhWJupggXW00Dlf9IJqthnlR'
bcrypt = Bcrypt(app) 

#params = urllib.parse.quote_plus('DRIVER={SQL SERVER};SERVER=10.140.12.55;DATABASE=DriftSide;UID=DriftAdmin;PWD=Nbdrift1881')
params = urllib.parse.quote_plus(f'{ServerCon}')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc:///?odbc_connect=%s' % params
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager(app)
login_manager.login_view = 'login' # telling the program where the login route is located, "View" is the route you need to login
login_manager.login_message_category = 'info'

app.config['CKEDITOR_PKG_TYPE'] = 'standard'
ckeditor = CKEditor(app)



from nb_driftApp import routes