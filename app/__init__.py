from flask import Flask
from flask_ask import Ask

application = Flask(__name__)
ask = Ask(application, "/")
