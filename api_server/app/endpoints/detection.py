"""mocked detections: just for testing"""
# from flask import Blueprint, jsonify
# detection_bp = Blueprint("detection", __name__)
# @detection_bp.route("/", methods=["POST"])
# def detect_frame():
#     # mock response
#     return jsonify({
#         "frame_id": "mock-0001",
#         "detections": [
#             {"id": 1, "label": "person", "bbox": [100, 120, 60, 180], "score": 0.98}
#         ],
#     })

from flask import Blueprint, jsonify, request
from pathlib import Path
from api_server.app.core import cpp_bridge

detection_bp = Blueprint("detection", __name__, url_prefix="/v1/detect")

@detection_bp.route("/", methods=["POST"])
def detect_route():
    image_path = request.json.get("image_path", "")

    # If no image path provided, use default test image
    if not image_path:
        default_image = Path(__file__).resolve().parent.parent.parent / "data" / "cache" / "test.jpg"
        if default_image.exists():
            image_path = str(default_image)
        else:
            return jsonify({"error": "No image path provided and no default test image found"}), 400

    try:
        detections = cpp_bridge.detect(image_path)
        return jsonify({"detections": detections})
    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 400
