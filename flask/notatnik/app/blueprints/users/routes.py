from flask import jsonify, abort

from . import users_bp

users = [
    {"id": 1, "name": "Anna Kowalska", "email": "anna@example.com"},
    {"id": 2, "name": "Jan Nowak", "email": "jan@example.com"},
    {"id": 3, "name": "Maria Wiśniewska", "email": "maria@example.com"},
]

@users_bp.route("/")
def get_users():
    # users  = [{id: }, {id: }, {} ]
    return jsonify(users)

@users_bp.route("/<int:user_id>")
def get_user(user_id):
    for user in users:
        if user['id'] == user_id:
            return jsonify(user)
    return abort(404)