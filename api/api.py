from flask import Flask, render_template, Blueprint


api_bp = Blueprint('api_bp', __name__,
    template_folder='templates',
    static_folder='static', static_url_path='assets')
