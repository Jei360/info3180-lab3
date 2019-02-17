from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525' # (or try 2525)
app.config['MAIL_USERNAME'] = '5b3c6bd3342561'
app.config['MAIL_PASSWORD'] = '22ee6e993f5816'
mail = Mail(app)
from app import views