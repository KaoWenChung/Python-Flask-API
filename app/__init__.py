from flask import Flask

app = Flask(__name__)

from app import routes






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