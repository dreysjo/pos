from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/shop_invoice'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
class Products(db.Model):
    product_id = db.Column(db.Integer(), primary_key=True)
    product_name = db.Column(db.String(255))
    product_price = db.Column(db.String(255))
    product_category = db.Column(db.String(255))

    def __init__(self, product_id, product_name, product_price, product_category):
            self.product_id = product_id
            self.product_name = product_name
            self.product_price = product_price
            self.product_category = product_category

class ProductsSchema(ma.Schema):
    class Meta:
        fields = ('product_id', 'product_name', 'product_price', 'product_category')

product_schema = ProductsSchema()
products_schema = ProductsSchema(many=True)

@app.route('/get_products', methods = ['get'])
def get_products():
    all_products = Products.query.all()
    results = products_schema.dump(all_products)
    return jsonify(results)

@app.route('/get_products/<id>/', methods = ['get'])
def product_details(product_id):
    product = Products.query.get(product_id)
    return product_schema.jsonify(product)

class Sales(db.Model):
    invoice_no = db.Column(db.Integer(), primary_key=True)
    total = db.Column(db.String(255))
    discount = db.Column(db.String(255))
    grand_total = db.Column(db.String(255))
    username = db.Column(db.String(255))

    def __init__(self, invoice_no, total, discount, grand_total, username):
        self.invoice_no = invoice_no
        self.total = total
        self.discount = discount
        self.grand_total = grand_total
        self.username = username


class SalesSchema(ma.Schema):
    class Meta:
        fields = ('invoice_no', 'total', 'discount', 'grand_total', 'username')

sales_schema = SalesSchema()
sales_many = SalesSchema(many=True)

@app.route('/get', methods = ['get'])
def get_sales():
    all_sales = Sales.query.all()
    results = sales_many.dump(all_sales)
    return jsonify(results)

@app.route('/get/<id>/', methods = ['get'])
def sales_details(invoice_no):
    sales = Sales.query.get(invoice_no)
    return sales_schema.jsonify(sales)

@app.route('/add', methods = ['post'])
def add_sales():
    total = request.json['total']
    discount = request.json['discount']
    grand_total = request.json['grand_total']
    username = request.json['username']

    # sales = Sales(total, discount, grand_total, username)
    sales = Sales('45896', '5', '45687', 'udey')
    db.session.add(sales)
    db.session.commit()
    return sales_schema.jsonify(sales)
#
# @app.route('/update/<id>/', methods = ['put'])
# def update_article(id):
#     article = Products.query.get(id)
#     title = request.json['title']
#     description = request.json['description']
#
#     article.title = title
#     article.description = description
#
#     db.session.commit()
#     return article_schema.jsonify(article)
#
# @app.route('/delete/<id>/', methods = ['Delete'])
# def article_delete(id):
#     article = Products.query.get(id)
#     db.session.delete(article)
#     db.session.commit()
#     return article_schema.jsonify(article)

if __name__ == '__main__':
    app.run(debug=True)