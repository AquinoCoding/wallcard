from flask import Flask, render_template
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

from app import routes
