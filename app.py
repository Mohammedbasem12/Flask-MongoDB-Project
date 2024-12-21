from flask import Flask, request, jsonify
from pymongo import MongoClient, errors
import os

app = Flask(__name__)

# MongoDB Connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["bookstore"]
collection = db["books"]

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not Found"}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal Server Error"}), 500

# POST /create: Insert data into MongoDB
@app.route("/create", methods=["POST"])
def create_book():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Invalid input"}), 400
        collection.insert_one(data)
        return jsonify({"message": "Book created successfully!"}), 201
    except errors.PyMongoError as e:
        return jsonify({"error": str(e)}), 500

# GET /read: Fetch data from MongoDB
@app.route("/read", methods=["GET"])
def read_books():
    try:
        books = list(collection.find({}, {"_id": 0}))  # Exclude MongoDB's `_id` field
        return jsonify(books), 200
    except errors.PyMongoError as e:
        return jsonify({"error": str(e)}), 500

# PUT /update: Update a record in MongoDB
@app.route("/update", methods=["PUT"])
def update_book():
    try:
        data = request.json
        if not data or not data.get("query") or not data.get("update"):
            return jsonify({"error": "Invalid input"}), 400
        result = collection.update_one(data["query"], {"$set": data["update"]})
        if result.matched_count == 0:
            return jsonify({"error": "No document found matching the query"}), 404
        return jsonify({"message": "Book updated successfully!"}), 200
    except errors.PyMongoError as e:
        return jsonify({"error": str(e)}), 500

# DELETE /delete: Delete a record from MongoDB
@app.route("/delete", methods=["DELETE"])
def delete_book():
    try:
        query = request.json
        if not query:
            return jsonify({"error": "Invalid input"}), 400
        result = collection.delete_one(query)
        if result.deleted_count == 0:
            return jsonify({"error": "No document found matching the query"}), 404
        return jsonify({"message": "Book deleted successfully!"}), 200
    except errors.PyMongoError as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def home():
    return "Welcome to the Flask API! Use the endpoints for CRUD operations."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)
