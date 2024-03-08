import os
from dotenv import load_dotenv
import requests
import json
from flask import Flask, request

load_dotenv()


def create_app():
    app = Flask(__name__)

    return app

create_app()