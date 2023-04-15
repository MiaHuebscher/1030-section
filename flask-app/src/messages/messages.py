from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


messages = Blueprint('messages', __name__)

# Write a message to a sublessor about a specific post
@messages.route('/messages', methods=['POST'])
def create_message():

    # Access json data from request object
    current_app.logger.info('Processing form data')
    req_data = request.get_json()
    current_app.logger.info(req_data)

    post_id = req_data['post_id']
    sblett_user = req_data['sblett_user']
    sbless_user = req_data['sbless_user']
    content = req_data['content']

    # Construct the insert statement
    insert_stmt = 'INSERT INTO messages (post_id, sblett_user, sbless_user, content) VALUES ('
    insert_stmt += str(post_id) + ', "' + sblett_user + '", "' + sbless_user + '", "' + content + '")'

    current_app.logger.info(insert_stmt)

    # Execute the query
    cursor = db.get_db().cursor()
    cursor.execute(insert_stmt)
    db.get_db().commit()
    return 'Success'

@messages.route('/messages/<post_id>/<sblett_user>', methods=['GET'])
def get_messages(post_id, sblett_user):
    # Get a cursor object from the database
    cursor = db.get_db().cursor()

    # Use cursor to query the database for a list of products
    cursor.execute('select post_id, sbless_user, sblett_user, content from messages \
                   where post_id = {0} and sblett_user = {}'.format(post_id, sblett_user))
    
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
    
