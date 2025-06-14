from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {"id": 1, "name": "Alice", "score": 90},
    {"id": 2, "name": "Bob", "score": 85}
]

# home
@app.route('/')
def home():
    return "Welcome to our API class"

@app.route('/data', methods=['GET'])
def data():
    return jsonify(students)


if __name__=="__main__":
    app.run()