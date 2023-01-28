from store import app, db
from store.Models import User, Product

with app.app_context():
    print(Product.query.all())
    for i in Product.query.all():
        print(i.image)
