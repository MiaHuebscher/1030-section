from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


subletters = Blueprint('subletters', __name__)

# Add a sublettor profile to the database
@subletters.route('/subletters', methods=['POST'])
def create_subletter_profile():
    pass

# Delete a sublettor profile from the database
@subletters.route('/subletters/<sblett_id>', methods=['DELETE'])
def delete_subletter(sblett_id):
    pass

# Update a sublettor profile in the database
@subletters.route('/subletters/<sblett_id>', methods=['PUT'])
def update_subletter_profile(sblett_id):
    pass