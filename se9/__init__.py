__version__ = "0.0.1"

import logging
logger = logging.getLogger(__name__)

import os

from flask import render_template
from jinja2 import TemplateNotFound

from pymongo import MongoClient

import connexion
from connexion.resolver import RestyResolver

DB       = os.environ.get("MONGODB_URI", "mongodb://localhost:27017/se9")
mongo    = MongoClient(DB)
database = DB.split("/")[-1]
db       = mongo[database]
app      = connexion.FlaskApp(__name__)
server   = app.app

app.add_api("se9.yaml", resolver=RestyResolver("se9"))

def render(template, **kwargs):
  try:
    return render_template(template + ".html", version=__version__, **kwargs)
  except TemplateNotFound:
    return render_template("404.html")

@server.route("/")
def render_home():
  return render("index")
