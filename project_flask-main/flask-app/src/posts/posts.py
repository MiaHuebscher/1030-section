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
    emp_id = req_data['emp_id']
    street = req_data['street']
    city = req_data['city']
    zip_code = req_data['zip_code']
    move_in = req_data['move_in']
    move_out = req_data['move_out']

    kitchen = req_data['kitchen']
    living_room = req_data['living_room']
    num_bedroom = req_data['num_bedroom']
    num_bathroom = req_data['num_bathroom']

    roommate_gender = req_data['roommate_gender']
    roommate_name = req_data['roommate_name']
    roommate_age = req_data['roommate_age']

    apartment_id = req_data['apartment_id']
    parking = req_data['parking']
    rec_center = req_data['rec_center']
    mail_room = req_data['mail_room']
    guard = req_data['guard']
    laundry = req_data['laundry']
    wifi = req_data['wifi']
    electricity = req_data['electricity']
    hot_water = req_data['hot_water']

    # Construct the insert statements for each table
    posts_insert_stmt = 'INSERT INTO posts \
        (sbless_id, post_dscrptn, unit_price, emp_id, street, city, zip_code, move_in, move_out) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
    posts_insert_params = (sbless_id, post_dscrptn, unit_price, emp_id, street, city, zip_code, move_in, move_out)
  
    current_app.logger.info(posts_insert_stmt)
    cursor = db.get_db().cursor()
    # Execute the query
    cursor.execute(posts_insert_stmt, posts_insert_params)
    post_id = cursor.lastrowid

    ap_units_insert_stmt = 'INSERT INTO apartment_units \
        (kitchen, living_room, num_bedroom, num_bathroom, post_id) VALUES (%s, %s, %s, %s, %s)'
    ap_units_insert_params = (kitchen, living_room, num_bedroom, num_bathroom, post_id)

    roommates_insert_stmt = 'INSERT INTO roommates (roommate_gender, post_id, roommate_name, roommate_age) VALUES (%s, %s, %s, %s)'
    roommates_insert_params = (roommate_gender, post_id, roommate_name, roommate_age)

    # # # photos_insert_stmt = ''
    # # # photos_insert_stmt += ''

    amenities_insert_stmt = 'INSERT INTO amenities \
        (apartment_id, parking, rec_center, mail_room, guard, laundry, wifi, electricity, hot_water) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
    amenities_insert_params = (apartment_id, parking, rec_center, mail_room, guard, laundry, wifi, electricity, hot_water)

    current_app.logger.info(ap_units_insert_stmt)
    current_app.logger.info(roommates_insert_stmt)
    # # current_app.logger.info(photos_insert_stmt)
    current_app.logger.info(amenities_insert_stmt)

    
    # Execute the query
    cursor.execute(ap_units_insert_stmt, ap_units_insert_params)
    cursor.execute(roommates_insert_stmt, roommates_insert_params)
    # # cursor.execute(photos_insert_stmt)
    cursor.execute(amenities_insert_stmt, amenities_insert_params)
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


# Delete a specific post that a sublessor wants to delete
@posts.route('/posts/<post_id>', methods=['DELETE'])
def delete_specific_post(post_id):

    # Access json data from request object
    current_app.logger.info('Processing form data')
    req_data = request.get_json()
    current_app.logger.info(req_data)

    delete_stmt = 'DELETE FROM subletters WHERE sublett_id = ' + str(post_id)

    current_app.logger.info(delete_stmt)

    # Execute the query
    cursor = db.get_db().cursor()
    cursor.execute(delete_stmt)
    db.get_db().commit()

    return 'Success'


# Delete a specific post that a sublessor wants to delete
@posts.route('/posts/<sbless_id>', methods=['DELETE'])
def delete_posts_by_sbless(sbless_id):

    # Access json data from request object
    current_app.logger.info('Processing form data')
    req_data = request.get_json()
    current_app.logger.info(req_data)

    delete_stmt = 'DELETE FROM subletters WHERE sublett_id = ' + str(sbless_id)

    current_app.logger.info(delete_stmt)

    # Execute the query
    cursor = db.get_db().cursor()
    cursor.execute(delete_stmt)
    db.get_db().commit()

    return 'Success'
