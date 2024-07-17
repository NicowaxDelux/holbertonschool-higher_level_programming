#!/usr/bin/python3
from flask import Flask, render_template, request
import csv, json

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

@app.route('/products')
def display_products():
    source = request.args.get('source')
    id = request.args.get('id')
    
    if source == 'json':
        products = read_json_file('products.json')
    elif source == 'csv':
        products = read_csv_file('products.csv')
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