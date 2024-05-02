from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample product data
products = [
    {"id": 1, "name": "Product 1", "price": 10.99, "description": "Description 1"},
    {"id": 2, "name": "Product 2", "price": 20.99, "description": "Description 2"},
    {"id": 3, "name": "Product 3", "price": 15.99, "description": "Description 3"}
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/product', methods=['POST'])
def create_product():
    data = request.json
    if not all(key in data for key in ('name', 'price', 'description')):
        return jsonify({'error': 'Missing parameters'}), 400
    product = {
        'id': len(products) + 1,
        'name': data['name'],
        'price': data['price'],
        'description': data['description']
    }
    products.append(product)
    return jsonify(product), 201

@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    global products
    products = [product for product in products if product['id'] != id]
    return jsonify({'message': 'Product deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)