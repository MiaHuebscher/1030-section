from flask import Blueprint, request, jsonify, make_response
import json
from src import db


products = Blueprint('products', __name__)

# Get all the products from the database
@products.route('/products', methods=['GET'])
def get_products():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute('SELECT id, product_code, product_name, list_price FROM products')

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# get the top 5 products from the database
@products.route('/mostExpensive')
def get_most_pop_products():
    cursor = db.get_db().cursor()
    query = '''
        SELECT product_code, product_name, list_price, reorder_level
        FROM products
        ORDER BY list_price DESC
        LIMIT 5
    '''
    cursor.execute(query)
       # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

@products.route('/product', methods=['POST'])
def add_new_product():
    # Access json data from request object
    current_app.logger.info('Processing form data')
    req_data = request.get_json()
    current_app.logger.info(req_data)

    prod_name = req_data['product_name']
    prod_description = req_data['product_description']
    prod_price = req_data['product_listprice']
    category = req_data['product_category']

    # Construct the insert statement
    insert_stmt = 'INSERT INTO products (product_name, description, category, list_price) VALUES ("'
    insert_stmt += prod_name + '", "' + prod_description + '", "' + category + '", ' + str(prod_price) + ')'

    current_app.logger.info(insert_stmt)

    # Execute the query
    cursor = db.get_db().cursor()
    cursor.execute(insert_stmt)
    db.get_db().commit()
    return 'Success'

@products.route('/categories', methods= ['GET'])
def get_all_categories():
    query = '''
        SELECT DISTINCT category AS label, category as value
        FROM products
        WHERE category IS NOT NULL
        ORDER BY category
        '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)

    json_data = []

    column_headers = [x[0] for x in cursor.description]
    theData = cursor.fetchall()

    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)