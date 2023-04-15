from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

posts = Blueprint('posts', __name__)

# Create a post about an subletting opportunity
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