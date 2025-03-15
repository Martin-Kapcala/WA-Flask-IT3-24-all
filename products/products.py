from flask import Flask, render_template, Blueprint

#Vstupní data simulující databázi
items = [
{"id": 1, "nazev": "Dell Latitude 5421", "cena": 25000, "popis": "Krátky popis počítače"},
{"id": 2, "nazev": "Acer Swift", "cena": 20000, "popis": "Základní notebook"},
{"id": 3, "nazev": "Linx PC sestava", "cena": 60000, "popis": "Herní mašina, která se nezadýchá..."},
{"id": 4, "nazev": "Testovací produkt", "cena": 99999, "popis": "Herní mašina, která se nezadýchá..."}
]



products_bp = Blueprint('products_bp', __name__,
    template_folder='templates',
    static_folder='static', static_url_path='assets')


@products_bp.route("/")
def home():
    return render_template("/products.html", products = items)

@products_bp.route("/<int:product_id>")
def detail(product_id):

    product = items[product_id-1]
    return render_template("/products-detail.html", product = product)