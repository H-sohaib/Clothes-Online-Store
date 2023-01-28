from store import app, db
from store.Models import User, Product

with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.add(Product(name='cluth', price=25,
                   clothes_type='jackets', image='item1.png', quantity=50))
    db.session.add(Product(name='jacket',
                   price=30, clothes_type='jackets', image='item2.png', quantity=10))
    db.session.add(Product(name='T-shurt', price=85,
                   clothes_type='jackets', image='item3.png', quantity=40))
    db.session.add(Product(name='jacket noir', price=10,
                   clothes_type='jackets', image='item4.png', quantity=30))
    db.session.add(Product(name='custom', price=1000,
                   clothes_type='jackets', image='item1.png', quantity=100))

    db.session.commit()
