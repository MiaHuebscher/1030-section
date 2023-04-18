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

# Delete a sublettor profile from the database
@subletters.route('/subletters/<sblett_id>', methods=['DELETE'])
def delete_subletter(sblett_id):
    subletter = Subletter.query.get(sblett_id)
    if not subletter:
        return jsonify({'error': 'Subletter not found'}), 404
    
    # Delete the subletter from the database
    db.session.delete(subletter)
    db.session.commit()

    # Return a JSON response indicating success
    return jsonify({'success': True})

    

# Update a sublettor profile in the database
@subletters.route('/subletters/<sblett_id>', methods=['PUT'])
def update_subletter_profile(sblett_id):

    subletter = Subletter.query.get(sblett_id)
    if not subletter:
        return jsonify({'error': 'Subletter not found'}), 404
    
    # Update the subletter with the new information
    subletter.sublett_id = request.json.get('sublett_id', subletter.sublett_id)
    subletter.sblett_user = request.json.get('sblett_user', subletter.sblett_user)
    subletter.sblett_age = request.json.get('sblett_age', subletter.sblett_age)
    subletter.sblett_gender = request.json.get('sblett_gender', subletter.sblett_gender)

    # Commit the changes to the database
    db.session.commit()

    # Return a JSON response indicating success
    return jsonify({'success': True})


