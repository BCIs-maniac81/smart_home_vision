from flask import Flask
from api_server.app.endpoints.detection import detection_bp
from api_server.app.endpoints.management import management_bp
from api_server.app.endpoints.streaming import streaming_bp


def create_app():
	app = Flask(__name__)

	# Register blueprints
	app.register_blueprint(detection_bp, url_prefix="/v1/detect")
	app.register_blueprint(management_bp, url_prefix="/v1/management")
	app.register_blueprint(streaming_bp, url_prefix="/v1/stream")

	return app

# Flask CLI entry
app = create_app()