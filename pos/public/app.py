from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_marshmallow import Marshmallow

app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flask'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/shop_invoice'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
class Products(db.Model):
    product_id = db.Column(db.Integer(), primary_key=True)
    product_name = db.Column(db.String(255))
    product_price = db.Column(db.String(255))
    product_category = db.Column(db.String(255))

    def __init__(self, title, description):
        self.title = title
        self.description = description

class ProductsSchema(ma.Schema):
    class Meta:
        fields = ('product_id', 'product_name', 'product_price', 'product_category')

product_schema = ProductsSchema()
products_schema = ProductsSchema(many=True)

@app.route('/get', methods = ['get'])
def get_products():
    all_products = Products.query.all()
    results = products_schema.dump(all_products)
    return jsonify(results)

@app.route('/get/<id>/', methods = ['get'])
def product_details(product_id):
    product = Products.query.get(product_id)
    return product_schema.jsonify(product)

# @app.route('/add', methods = ['post'])
# def add_article():
#     title = request.json['title']
#     description = request.json['description']
#
#     articles = Products(title, description)
#     db.session.add(articles)
#     db.session.commit()
#     return article_schema.jsonify(articles)
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