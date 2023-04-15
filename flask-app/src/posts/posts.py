from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

posts = Blueprint('posts', __name__)

# Create a post about a subletting opportunity
@posts.route('/posts', methods=['POST'])
def create_post():
    # Access json data from request object
    current_app.logger.info('Processing form data')
    req_data = request.get_json()
    current_app.logger.info(req_data)

    # Change this stuff to the variables that will be inserted into the tables 
    sbless_id = req_data['sbless_id']
    post_dscrptn = req_data['post_dscrptn']
    unit_price = req_data['unit_price']
    emp_id = None
    street = req_data['street']
    city = req_data['city']
    zip_code = req_data['zip_code']
    move_in = req_data['move_in']
    move_out = req_data['move_out']

    # Construct the insert statements for each table
    posts_insert_stmt = 'INSERT INTO posts \
        (sbless_id, post_dscrptn, unit_price, emp_id, street, city, zip_code, move_in, move_out) VALUES ('
    posts_insert_stmt += str(post_id) + ', "' + sblett_user + '", "' + sbless_user + '", "' + content + '")'

    ap_units_insert_stmt = ''
    ap_units_insert_stmt += ''

    roommates_insert_stmt = ''
    roommates_insert_stmt += ''

    photos_insert_stmt = ''
    photos_insert_stmt += ''

    amenities_insert_stmt = ''
    amenities_insert_stmt += ''

    current_app.logger.info(posts_insert_stmt)
    current_app.logger.info(ap_units_insert_stmt)
    current_app.logger.info(roommates_insert_stmt)
    current_app.logger.info(photos_insert_stmt)
    current_app.logger.info(amenities_insert_stmt)

    # Execute the query
    cursor = db.get_db().cursor()
    cursor.execute(posts_insert_stmt)
    cursor.execute(ap_units_insert_stmt)
    cursor.execute(roommates_insert_stmt)
    cursor.execute(photos_insert_stmt)
    cursor.execute(amenities_insert_stmt)
    db.get_db().commit()
    return 'Success'

# Get a list of all the posts in the database and their corresponding information
@posts.route('/posts', methods=['GET'])
def get_posts():

    # Get a cursor object from the database
    cursor = db.get_db().cursor()

    # Use cursor to query the database for a list of products
    cursor.execute('SELECT post_id, post_dscrptn, unit_price, emp_id, street, city, zip_code, move_in, move_out FROM posts')

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
    return cursor.description

# Get information about a specific posts
@posts.route('/posts/<post_id>', methods=['GET'])
def get_specific_post(post_id):
    cursor = db.get_db().cursor()
    cursor.execute('select post_id, post_dscrptn, unit_price, emp_id, street, city, zip_code, move_in, move_out \
                    from posts where post_id = {0}'.format(post_id))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get information about a posts under a specified price
@posts.route('/posts/<unit_price>', methods=['GET'])
def get_inexpensive_posts(unit_price):
    cursor = db.get_db().cursor()
    cursor.execute('select post_id, post_dscrptn, unit_price, emp_id, street, city, zip_code, move_in, move_out \
                    from customers where unit_price <= {0}'.format(unit_price))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
