#!/usr/bin/python3
from flask import Flask, render_template, request
import csv, json, sqlite3

app = Flask(__name__)

def read_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def read_csv_file(filename):
    data = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def read_sqlite_data():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()
    products = [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in rows]
    return products


@app.route('/products')
def display_products():
    source = request.args.get('source')
    id = request.args.get('id')
    
    if source == 'json':
        products = read_json_file('products.json')
    elif source == 'csv':
        products = read_csv_file('products.csv')
    elif source == 'sql':
        products = read_sqlite_data()
    else:
        return render_template('product_display.html', error='Wrong source')
    
    if id:
        filtered_products = [product for product in products if str(product['id']) == id]
        if not filtered_products:
            return render_template('product_display.html', error='Product not found')
        products = filtered_products
    
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)