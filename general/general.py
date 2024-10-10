from flask import Flask, render_template, Blueprint


general_bp = Blueprint('general_bp', __name__,
    template_folder='templates',
    static_folder='static')

#Musíme ještě upravit!!!
@general_bp.route("/")
def home():
    return render_template("general/index.html")