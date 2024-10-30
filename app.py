from flask import Flask, render_template

#Import mého blueprintu z modulu
from general.general import general_bp
from products.products import products_bp
from api.api import api_bp

app = Flask(__name__)

#Registrace blueprintu - takto o něm bude Flask vědět
app.register_blueprint(general_bp)
app.register_blueprint(products_bp, url_prefix="/products")
#app.register_blueprint(api_bp)


if __name__ == "__main__":
    app.run(debug=True)