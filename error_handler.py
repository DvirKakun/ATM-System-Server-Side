from flask import jsonify
from werkzeug.exceptions import HTTPException

def init_error_handler(app):
    """
      Registers a global error handler for the Flask application.

      This function intercepts exceptions and ensures that all errors are returned as JSON responses.

      Args:
          app (Flask): The Flask application instance.

      Returns:
          JSON response with an appropriate error message and HTTP status code.
      """

    @app.errorhandler(Exception)
    def handle_errors(error):
        """
         Handles both expected HTTP errors and unexpected server errors.

         - If the error is an instance of `HTTPException`, return its details.
         - Otherwise, return a generic 500 Internal Server Error message.

         Args:
             error (Exception): The exception that was raised.

         Returns:
             Response: A JSON response containing the error details and HTTP status code.
         """

        if isinstance(error, HTTPException):  # If it's an HTTP error (like 400, 404, 415)
            return jsonify({"error": error.name, "message": str(error.description)}), error.code
        else:  # If it's some unexpected server error
            return jsonify({"error": "Internal Server Error", "message": "Please try again later"}), 500