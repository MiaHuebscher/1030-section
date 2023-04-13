from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


subletters = Blueprint('subletters', __name__)

# Add a sublettor profile to the database
@subletters.route('/subletters', methods=['POST'])
def create_subletter_profile():
    pass

    # Access json data from request object
    current_app.logger.info('Processing form data')
    req_data = request.get_json()
    current_app.logger.info(req_data)

    prod_name = req_data['product_name']
    prod_description = req_data['product_description']
    prod_price = req_data['product_listprice']
    category = req_data['product_category']

    # Construct the insert statement
    insert_stmt = 'INSERT INTO subletters (product_name, description, category, list_price) VALUES ("'
    insert_stmt += prod_name + '", "' + prod_description + '", "' + category + '", ' + str(prod_price) + ')'

    current_app.logger.info(insert_stmt)

    # Execute the query
    cursor = db.get_db().cursor()
    cursor.execute(insert_stmt)
    db.get_db().commit()

    return 'Success'

# Delete a sublettor profile from the database
@subletters.route('/subletters/<sblett_id>', methods=['DELETE'])
def delete_subletter(sblett_id):
    pass

# Update a sublettor profile in the database
@subletters.route('/subletters/<sblett_id>', methods=['PUT'])
def update_subletter_profile(sblett_id):
    pass