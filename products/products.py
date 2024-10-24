from flask import Flask, render_template, Blueprint


products_bp = Blueprint('products_bp', __name__,
    template_folder='templates',
    static_folder='static', static_url_path='assets')

#Musíme ještě upravit!!!
@products_bp.route("/")
def home():
    return render_template("/detail.html")