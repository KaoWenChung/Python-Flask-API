from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models






# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Home"

# # GET API request
# @app.route("/get-user/<user_id>")
# def get_user(user_id):
#     user_data = {
#         "user_id": user_id,
#         "name": "Mike",
#         "email": "mike.mock@example.com"
#     }

#     extra = request.args.get("extra")
#     if extra:
#         user_data["extra"] = extra

#     return jsonify(user_data), 200

# # POST API request
# @app.route("/create-user", methods=["POST"])
# def create_user():
#     data = request.get_json()

#     return jsonify(data), 201

# if __name__ == "__main__":
#     app.run(debug=True)