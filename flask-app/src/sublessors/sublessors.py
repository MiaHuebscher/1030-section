from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

sublessors = Blueprint('sublessors', __name__)

# Create a post about a subletting opportunity
@sublessors.route('/posts', methods=['POST'])
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

    current_app.logger.info(ap_units_insert_stmt)
    current_app.logger.info(roommates_insert_stmt)
    
    # Execute the query
    cursor.execute(ap_units_insert_stmt, ap_units_insert_params)
    cursor.execute(roommates_insert_stmt, roommates_insert_params)
    # # cursor.execute(photos_insert_stmt)
    # cursor.execute(amenities_insert_stmt, amenities_insert_params)
    db.get_db().commit()
    return 'Success'


# Get a list of all the posts in the database and their corresponding information
@sublessors.route('/posts', methods=['GET'])
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
@sublessors.route('/posts/<post_id>', methods=['GET'])
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
@sublessors.route('/posts/<unit_price>', methods=['GET'])
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


# Update a sublessor profile in the database
@sublessors.route('/posts/post_dscrptn/<post_id>', methods=['PUT'])
def update_post(post_id):

    # Access json data from request object
    current_app.logger.info('Processing form data')
    req_data = request.get_json()
    current_app.logger.info(req_data)

    post_dscrptn = req_data['post_dscrptn2']

    if post_dscrptn != '': 
        update_post_dscrptn = 'UPDATE posts SET post_dscrptn = '  + '"' + post_dscrptn + '"' 
        update_post_dscrptn += 'WHERE post_id =' + str(post_id)

        current_app.logger.info(update_post_dscrptn)

        # Execute the query
        cursor = db.get_db().cursor()
        cursor.execute(update_post_dscrptn)
        db.get_db().commit()

        return 'Success'


# Delete a specific post that a sublessor wants to delete
@sublessors.route('/posts/<post_id>', methods=['DELETE'])
def delete_specific_post(post_id):

    delete_stmt = 'DELETE FROM posts WHERE post_id = ' + str(post_id)

    current_app.logger.info(delete_stmt)

    # Execute the query
    cursor = db.get_db().cursor()
    cursor.execute(delete_stmt)
    db.get_db().commit()

    return 'Success'


# Delete a specific post that a sublessor wants to delete
@sublessors.route('/posts/sublessor/<sbless_id>', methods=['DELETE'])
def delete_posts_by_sbless(sbless_id):

    delete_stmt = 'DELETE FROM posts WHERE sbless_id = ' + str(sbless_id)

    current_app.logger.info(delete_stmt)

    # Execute the query
    cursor = db.get_db().cursor()
    cursor.execute(delete_stmt)
    db.get_db().commit()

    return 'Success'

#jakob
@sublessors.route('/reviews/review_content/<sbless_user>', methods=['GET']) #question about get
def get_reviews(sbless_user):
   # Get a cursor object from the database
   cursor = db.get_db().cursor()


   # Use cursor to query the database for a list of products
   cursor.execute('select rev_content from reviews \
                  where sbless_user = {}'.format(sbless_user))
  
   # Grab the column headers from the returned data
   row_headers = [x[0] for x in cursor.description]


   # Create an empty object to use in putting column headers together with data
   json_data = []


   # Fetch all the data from the cursor
   theData = cursor.fetchall()


   # For each of the rows, zip the data elements together with the column headers.
   for row in theData:
       json_data.append(dict(zip(row_headers, row)))
  
   # Format the response and return it
   the_response = make_response(jsonify(json_data))
   the_response.status_code = 200
   the_response.mimetype = 'application/json'
   return the_response


@sublessors.route('/leases/<lease_id>', methods=['PUT'])
def update_lease_profile(lease_id):


   # Access json data from request object
   current_app.logger.info('Processing form data')
   req_data = request.get_json()
   current_app.logger.info(req_data)


   lease_end_date = req_data['lease_end_date']


   update_lease_end_date = 'UPDATE leases SET lease_end_date = ' + '"' + lease_end_date + '"'
   update_lease_end_date += 'WHERE lease_id =' + str(lease_id)

   current_app.logger.info(update_lease_end_date)

   # Execute the query
   cursor = db.get_db().cursor()
   cursor.execute(update_lease_end_date)
   db.get_db().commit()

   return 'Success'


@sublessors.route('/leases/<sbless_id>', methods=['POST'])
def create_sublessor_lease(sbless_id):


   # Access json data from request object
   current_app.logger.info('Processing form data')
   req_data = request.get_json()
   current_app.logger.info(req_data)


   lease_end_date = req_data['lease_end_date']
   lord_id = req_data['lord_id']
   lease_start_date = req_data['lease_start_date']
   rent = req_data['rent']


   # Construct the insert statement
   insert_stmt = 'INSERT INTO leases (lease_end_date, lord_id, lease_start_date, rent, sbless_id) VALUES ("'
   insert_stmt += lease_end_date + '", ' + str(lord_id) + ', "' + lease_start_date + '", ' + str(rent) + ', ' + str(sbless_id) + ')'


   current_app.logger.info(insert_stmt)


   # Execute the query
   cursor = db.get_db().cursor()
   cursor.execute(insert_stmt)
   db.get_db().commit()


   return 'Success'


@sublessors.route('/sublessors', methods=['POST'])
def create_sublessor_profile():


   # Access json data from request object
   current_app.logger.info('Processing form data')
   req_data = request.get_json()
   current_app.logger.info(req_data)


   sbless_user = req_data['sbless_user']
   sbless_id = req_data['sbless_id2']
   sbless_gender = req_data['sbless_gender']
   sbless_age = req_data['sbless_age']


   # Construct the insert statement
   insert_stmt = 'INSERT INTO sublessors (sbless_user, sbless_id, sbless_gender, sbless_age) VALUES ("'
   insert_stmt += sbless_user + '", ' + str(sbless_id) + ', "' + sbless_gender + '", ' + str(sbless_age) + ')'


   current_app.logger.info(insert_stmt)


   # Execute the query
   cursor = db.get_db().cursor()
   cursor.execute(insert_stmt)
   db.get_db().commit()


   return 'Success'


