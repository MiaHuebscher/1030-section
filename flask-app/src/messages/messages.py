from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


messages = Blueprint('messages', __name__)

# Write a message to a sublessor about a specific post
@messages.route('/messages/<post_id>/<sbless_user>', methods=['POST'])
def create_message(post_id, sbless_user):
    pass