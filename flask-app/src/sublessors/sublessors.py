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
   lease_id = req_data['lease_id']
   lord_id = req_data['lord_id']
   lease_start_date = req_data['lease_start_date']
   rent = req_data['rent']
   sbless_id = req_data['sbless_id']


   # Construct the insert statement
   insert_stmt = 'UPDATE leases SET (lease_end_date, lease_id,lord_id, lease_start_date, rent, sbless_id) VALUES ('
   insert_stmt += str(lease_end_date) + ', "' + lease_id + '", ' + lord_id + ', "' + str(lease_start_date)
   + ', "' + rent + ', "' + sbless_id + '")'


   current_app.logger.info(insert_stmt)


   # Execute the query
   cursor = db.get_db().cursor()
   cursor.execute(insert_stmt)
   db.get_db().commit()


   return 'Success'


@sublessors.route('/leases/<sbless_id>', methods=['POST'])
def create_sublessor_lease(sbless_id):


   # Access json data from request object
   current_app.logger.info('Processing form data')
   req_data = request.get_json()
   current_app.logger.info(req_data)


   lease_end_date = req_data['lease_end_date']
   lease_id = req_data['lease_id']
   lord_id = req_data['lord_id']
   lease_start_date = req_data['lease_start_date']
   rent = req_data['rent']


   # Construct the insert statement
   insert_stmt = 'INSERT INTO leases (lease_end_date, lease_id,lord_id, lease_start_date, rent, sbless_id) VALUES ('
   insert_stmt += str(lease_end_date) + ', "' + lease_id + '", ' + lord_id + ', "' + str(lease_start_date)
   + ', "' + rent + ', "' + sbless_id + '")'


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
   sbless_id = req_data['sbless_id']
   sbless_gender = req_data['sbless_gender']
   sbless_age = req_data['sbless_age']


   # Construct the insert statement
   insert_stmt = 'INSERT INTO sublessors (sbless_user, sbless_id, sbless_gender, sbless_age) VALUES ('
   insert_stmt += sbless_user + ', "' + sbless_id + '", ' + sbless_gender + ', "' + sbless_age + '")'


   current_app.logger.info(insert_stmt)


   # Execute the query
   cursor = db.get_db().cursor()
   cursor.execute(insert_stmt)
   db.get_db().commit()


   return 'Success'


