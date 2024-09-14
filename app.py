from flask import Flask, jsonify, request #jsonify: A helper function provided by Flask that converts Python dictionaries or lists into JSON responses.
from models import db, Category, Product, Customer, Order, OrderItem, Payment #import from models file the db and all classes(table)
from config import Config #import db connection from config file
app = Flask(__name__) #Create Flask Application Instance
app.config.from_object(Config) #Configure Flask Application
db.init_app(app) #Initialize Database
#API Routes(endpoints)
@app.route('/', methods=['GET'])#without endpoint
def home():
    categories = Category.query.all()
    return jsonify([{'category_id': c.category_id, 'name': c.name, 'description': c.description} for c in categories])
@app.route('/categories', methods=['GET']) #First endpoint with GET request 
def get_categories():
    categories = Category.query.all() #get all data from category table
    return jsonify([{'category_id': c.category_id, 'name': c.name, 'description': c.description} for c in categories]) # create a JSON response from a list of Python dictionaries

@app.route('/products', methods=['GET']) #Second endpoint
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

@app.route('/customers', methods=['GET']) #Third endpoint
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

@app.route('/orders', methods=['GET']) #4th endpoint
def get_orders():
    orders = Order.query.all()
    return jsonify([{
        'order_id': o.order_id,
        'customer_id': o.customer_id,
        'order_date': o.order_date.isoformat(),
        'total': str(o.total),
        'status': o.status
    } for o in orders])

@app.route('/order_items', methods=['GET']) #5th endpoint
def get_order_items():
    order_items = OrderItem.query.all()
    return jsonify([{
        'order_item_id': oi.order_item_id,
        'order_id': oi.order_id,
        'product_id': oi.product_id,
        'quantity': oi.quantity,
        'price': str(oi.price)
    } for oi in order_items])

@app.route('/payments', methods=['GET']) #6th endpoint
def get_payments():
    payments = Payment.query.all()
    return jsonify([{
        'payment_id': p.payment_id,
        'order_id': p.order_id,
        'payment_date': p.payment_date.isoformat(),
        'amount': str(p.amount),
        'payment_method': p.payment_method
    } for p in payments])

#Route to add a new customer
@app.route('/customers', methods=['POST']) #7th endpoint with POST REQUEST(you need postman or cURL)
def create_customer():
    data = request.get_json() #Retrieves the JSON data sent in the body of the POST request and parses it into a Python dictionary.
    new_customer = Customer( #Creates a new instance of the Customer model with the data extracted from the request.
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        phone=data.get('phone'),
        address=data.get('address')
    )
    db.session.add(new_customer) #it is scheduled to be inserted into the database when the session is committed.
    db.session.commit() #Commits the transaction to the database
    return jsonify({'message': 'Customer created successfully'}), 201 #Returns a JSON response to the client indicating that the customer was created successfully

if __name__ == '__main__': #block in Python is used to execute some code only when the script is run directly, not when it is imported as a module.
    app.run(debug=True)
