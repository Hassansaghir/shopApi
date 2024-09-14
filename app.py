from flask import Flask, jsonify, request
from models import db, Category, Product, Customer, Order, OrderItem, Payment
from config import Config
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
#API Routes(endpoints)
@app.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([{'category_id': c.category_id, 'name': c.name, 'description': c.description} for c in categories])

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{
        'product_id': p.product_id, 
        'name': p.name, 
        'description': p.description, 
        'price': str(p.price), 
        'stock': p.stock, 
        'category_id': p.category_id
    } for p in products])

@app.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([{
        'customer_id': c.customer_id,
        'first_name': c.first_name,
        'last_name': c.last_name,
        'email': c.email,
        'phone': c.phone,
        'address': c.address
    } for c in customers])

@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([{
        'order_id': o.order_id,
        'customer_id': o.customer_id,
        'order_date': o.order_date.isoformat(),
        'total': str(o.total),
        'status': o.status
    } for o in orders])

@app.route('/order_items', methods=['GET'])
def get_order_items():
    order_items = OrderItem.query.all()
    return jsonify([{
        'order_item_id': oi.order_item_id,
        'order_id': oi.order_id,
        'product_id': oi.product_id,
        'quantity': oi.quantity,
        'price': str(oi.price)
    } for oi in order_items])

@app.route('/payments', methods=['GET'])
def get_payments():
    payments = Payment.query.all()
    return jsonify([{
        'payment_id': p.payment_id,
        'order_id': p.order_id,
        'payment_date': p.payment_date.isoformat(),
        'amount': str(p.amount),
        'payment_method': p.payment_method
    } for p in payments])

# Route to add a new customer
@app.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    new_customer = Customer(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        phone=data.get('phone'),
        address=data.get('address')
    )
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({'message': 'Customer created successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
