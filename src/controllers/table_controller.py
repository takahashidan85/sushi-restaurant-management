from flask import Blueprint, jsonify, request

table_bp = Blueprint("table", __name__)
tables = [
    {"id": 1, "number": 1, "status": "available"},
    {"id": 2, "number": 2, "status": "occupied"},
]

@table_bp.route("/", methods=["GET"])
def get_tables():
    return jsonify(tables)

@table_bp.route("/", methods=["POST"])
def add_table():
    data = request.json
    tables.append(data)
    return jsonify({"message": "Table added"}), 201
