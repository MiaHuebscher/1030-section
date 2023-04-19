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

    # Access json data from request object
    current_app.logger.info('Processing form data')
    req_data = request.get_json()
    current_app.logger.info(req_data)

    delete_stmt = 'DELETE FROM subletters WHERE sublett_id = ' + str(sblett_id)

    current_app.logger.info(delete_stmt)

    # Execute the query
    cursor = db.get_db().cursor()
    cursor.execute(delete_stmt)
    db.get_db().commit()

    return 'Success'


# Update a sublettor profile in the database
@subletters.route('/subletters/<sblett_id>', methods=['PUT'])
def update_subletter_profile(sblett_id):

    # Access json data from request object
    current_app.logger.info('Processing form data')
    req_data = request.get_json()
    current_app.logger.info(req_data)

    sblett_user = req_data['sblett_user']
    sblett_age = req_data['sblett_age']
    sblett_gender = req_data['sblett_gender']

    if sblett_user != '': 
        update_user_stmt = 'UPDATE subletters SET sblett_user = ' + '"' + sblett_user + '"' 
        update_user_stmt += 'WHERE sublett_id =' + str(sblett_id)

        current_app.logger.info(update_user_stmt)

        # Execute the query
        cursor = db.get_db().cursor()
        cursor.execute(update_user_stmt)
        db.get_db().commit()

        return 'Success'

    if sblett_age != '': 
        update_age_stmt = 'UPDATE subletters SET sblett_age = ' + str(sblett_age)
        update_age_stmt += 'WHERE sublett_id =' + str(sblett_id)

        current_app.logger.info(update_age_stmt)

        # Execute the query
        cursor = db.get_db().cursor()
        cursor.execute(update_age_stmt)
        db.get_db().commit()

        return 'Success'

        
    if sblett_gender != '': 
        update_gender_stmt = 'UPDATE subletters SET sblett_gender = ' + '"' + sblett_gender + '"'
        update_gender_stmt += 'WHERE sublett_id =' + str(sblett_id)

        current_app.logger.info(update_stmt)

        # Execute the query
        cursor = db.get_db().cursor()
        cursor.execute(update_gender_stmt)
        db.get_db().commit()


        return 'Success'