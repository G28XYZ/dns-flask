from flask import Flask
from config import Config

app = Flask(__name__)
# print('\n'.join(dir(app)))
#app.config.from_object(Config)

from app import routes