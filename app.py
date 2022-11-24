from flask import Flask, jsonify
from api.index import API_BLUEPRINT, loadEndpoints

# Create app
def create_app():
    app = Flask(__name__)

    # Ping route to test the app
    @app.route('/ping/')
    def ping():
        return jsonify({"status": "OK"})

    # Register API endpoints
    loadEndpoints()
    app.register_blueprint(API_BLUEPRINT)

    return app 


if __name__ == "__main__":
    app = create_app()
    app.run(host="127.0.0.1", port=8080, debug=True)
