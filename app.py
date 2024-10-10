from flask import Flask, render_template

#Import mého blueprintu z modulu general
from general.general import general_bp

app = Flask(__name__)

#Registrace blueprintu - takto o něm bude Flask vědět
app.register_blueprint(general_bp)
