from flask import Blueprint, jsonify

streaming_bp = Blueprint("streaming", __name__)

@streaming_bp.route("/<camera_id>", methods=["GET"])
def stream_info(camera_id):
    # stub
    return jsonify({"camera_id": camera_id, "stream": "not_implemented"})
