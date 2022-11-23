from flask import Flask, jsonify

# Create app
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return jsonify({"Hello": "World"})

    return app 


if __name__ == "__main__":
    app = create_app()
    app.run(host="127.0.0.1", port=8080, debug=True)
