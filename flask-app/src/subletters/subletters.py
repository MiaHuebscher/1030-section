from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


subletters = Blueprint('subletters', __name__)

# Add a sublettor profile to the database
@subletters.route('/subletters', methods=['POST'])
def create_subletter_profile():

    # Access json data from request object
    current_app.logger.info('Processing form data')
    req_data = request.get_json()
    current_app.logger.info(req_data)

    sublett_id = req_data['sublett_id']
    sblett_user = req_data['sblett_user']
    sblett_age = req_data['sblett_age']
    sblett_gender = req_data['sblett_gender']

    # Construct the insert statement
    insert_stmt = 'INSERT INTO subletters (sublett_id, sblett_user, sblett_age, sblett_gender) VALUES ('
    insert_stmt += str(sublett_id) + ', "' + sblett_user + '", ' + str(sblett_age) + ', "' + sblett_gender + '")'

    current_app.logger.info(insert_stmt)

    # Execute the query
    cursor = db.get_db().cursor()
    cursor.execute(insert_stmt)
    db.get_db().commit()

    return 'Success'


# Delete a sublettor profile in the database
@subletters.route('/subletters/<sblett_id>', methods=['DELETE'])
def delete_subletter(sblett_id):

    # Create and log the delete statement
    delete_stmt = 'DELETE FROM subletters WHERE sublett_id = ' + str(sblett_id)
    current_app.logger.info(delete_stmt)

    # Execute the query
    cursor = db.get_db().cursor()
    cursor.execute(delete_stmt)
    db.get_db().commit()

    return 'Success'

# Update a sublettor username in the database
@subletters.route('/subletters/<sblett_id>', methods=['PUT'])
def update_subletter_username(sblett_id):

    # Access json data from request object
    current_app.logger.info('Processing form data')
    req_data = request.get_json()
    current_app.logger.info(req_data)

    sblett_user = req_data['new_sblett_user']

    update_user_stmt = 'UPDATE subletters SET sblett_user = ' + '"' + sblett_user + '"' 
    update_user_stmt += 'WHERE sublett_id =' + str(sblett_id)

    current_app.logger.info(update_user_stmt)

    # Execute the query
    cursor = db.get_db().cursor()
    cursor.execute(update_user_stmt)
    db.get_db().commit()

    return 'Success'

# Send a messsage to another person on the app
@subletters.route('/messages', methods=['POST'])
def create_message():

    # Access json data from request object
    current_app.logger.info('Processing form data')
    req_data = request.get_json()
    current_app.logger.info(req_data)

    post_id = req_data['post_id']
    sblett_user = req_data['sblett_user']
    sbless_user = req_data['sbless_user']
    content = req_data['content']
    mess_from = req_data['mess_from']

    # Construct the insert statement
    insert_stmt = 'INSERT INTO messages (post_id, sblett_user, sbless_user, content, mess_from) VALUES ('
    insert_stmt += str(post_id) + ', "' + sblett_user + '", "' + sbless_user + '", "' + content + '", "' + mess_from + '")'

    current_app.logger.info(insert_stmt)

    # Execute the query
    cursor = db.get_db().cursor()
    cursor.execute(insert_stmt)
    db.get_db().commit()
    return 'Success'

# Get a list of all the messages related to a specific post from a specific sublessor
@subletters.route('/messages/<post_id>/<sblett_user>', methods=['GET'])
def get_messages(post_id, sblett_user):
    # Get a cursor object from the database
    cursor = db.get_db().cursor()

    # Use cursor to query the database for a list of products
    cursor.execute('select post_id, sbless_user, sblett_user, content from messages \
                   where post_id = {0} and sblett_user = {1}'.format(post_id, sblett_user))
    
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
    

# Get a list of all the posts in the database and their corresponding information
@subletters.route('/posts', methods=['GET'])
def get_posts():

    # Get a cursor object from the database
    cursor = db.get_db().cursor()

    # Use cursor to query the database for a list of products
    cursor.execute('SELECT post_id, sbless_user, post_dscrptn, unit_price, emp_id, street, city, \
       zip_code, move_in, move_out FROM posts join sublessors using (sbless_id)')

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
@subletters.route('/posts/<post_id>', methods=['GET'])
def get_specific_post(post_id):
    cursor = db.get_db().cursor()
    cursor.execute('select post_id, sbless_user, post_dscrptn, unit_price, emp_id, street, city, zip_code, move_in, move_out \
                    from posts join sublessors using (sbless_id) where post_id = {0}'.format(post_id))
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
@subletters.route('/postsunder/<unit_price>', methods=['GET'])
def get_inexpensive_posts(unit_price):
    cursor = db.get_db().cursor()

    query = "select post_id, sbless_user, post_dscrptn, unit_price, emp_id, street, city, zip_code, move_in, move_out \
                    from posts join sublessors using (sbless_id) where unit_price <= {}".format(unit_price)
    
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response
