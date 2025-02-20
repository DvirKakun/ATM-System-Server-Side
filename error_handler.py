from flask import jsonify
from werkzeug.exceptions import HTTPException

def init_error_handler(app):
    @app.errorhandler(Exception)
    def handle_errors(error):
        if isinstance(error, HTTPException):  # If it's an HTTP error (like 400, 404, 415)
            return jsonify({"error": error.name, "message": str(error.description)}), error.code
        else:  # If it's some unexpected server error
            return jsonify({"error": "Internal Server Error", "message": "Please try again later"}), 500