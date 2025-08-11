from flask import Blueprint, jsonify

management_bp = Blueprint("management", __name__)

@management_bp.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "ok", "component": "management"})
