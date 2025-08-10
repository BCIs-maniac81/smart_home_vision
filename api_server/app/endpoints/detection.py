from flask import Blueprint, jsonify

detection_bp = Blueprint("detection", __name__)

@detection_bp.route("/", methods=["POST"])
def detect_frame():
    # mock response
    return jsonify({
        "frame_id": "mock-0001",
        "detections": [
            {"id": 1, "label": "person", "bbox": [100, 120, 60, 180], "score": 0.98}
        ],
    })
