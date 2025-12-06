import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# --- Helper functions ---

def read_json_file(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return []

def read_csv_file(filename):
    try:
        products = []
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
        return products
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return []

def read_sqlite_db(filename):
    try:
        conn = sqlite3.connect(filename)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        products = []
        for row in rows:
            products.append({
                "id": row["id"],
                "name": row["name"],
                "category": row["category"],
                "price": row["price"]
            })
        conn.close()
        return products
    except Exception as e:
        print(f"Error reading SQLite DB: {e}")
        return None

# --- Flask route ---

@app.route('/products')
def products():
    source = request.args.get('source', 'json').lower()
    product_id = request.args.get('id', None)
    error = None
    products_list = []

    # Load data based on source
    if source == 'json':
        products_list = read_json_file('products.json')
    elif source == 'csv':
        products_list = read_csv_file('products.csv')
    elif source == 'sql':
        products_list = read_sqlite_db('products.db')
        if products_list is None:
            error = "Error reading database"
    else:
        error = "Wrong source"

    # Filter by ID if provided
    if product_id and not error:
        try:
            pid = int(product_id)
            products_list = [p for p in products_list if p['id'] == pid]
            if not products_list:
                error = "Product not found"
        except ValueError:
            error = "Invalid id"

    return render_template('product_display.html', products=products_list, error=error)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, port=5000)

