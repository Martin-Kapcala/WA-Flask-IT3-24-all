from flask import Flask, render_template, Blueprint


general_bp = Blueprint('general_bp', __name__,
    template_folder='templates',
    static_folder='static')

#Základní routa modulu, která vygeneruje hlavní stránku
@general_bp.route("/")
def home():
    return render_template("general/index.html")

#Routa o nás
@general_bp.route("/about")
def about():
    return render_template("general/about.html")

#Routa časté otázky a odpovědi
@general_bp.route("/faq")
def faq():
    return render_template("general/faq.html")

#Routa kontakt
@general_bp.route("/contact")
def contact():
    return render_template("general/contact.html")