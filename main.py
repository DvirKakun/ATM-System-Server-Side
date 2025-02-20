from flask import Flask
from routes import init_routes
from error_handler import init_error_handler
import os

app = Flask(__name__)
init_routes(app) # Initialize endpoints
init_error_handler(app) # Initialize error handler

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)