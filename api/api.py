from flask import Flask, render_template, Blueprint
import requests, json

api_bp = Blueprint('api_bp', __name__,
    template_folder='templates',
    static_folder='static', static_url_path='assets')

#URL prefix API
URL_PATH_API = "https://api.escuelajs.co/api/v1"

def GetAllProducts():
    result = requests.get(f"{URL_PATH_API}/products")

    return json.loads(result.text)