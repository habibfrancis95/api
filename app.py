from flask import Flask
from controllers import itemsController


app = Flask(__name__)


itemsController.initController(app)
