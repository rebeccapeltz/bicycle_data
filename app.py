from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/bicycle_sales', methods=['GET'])
def get_products():
    with open("bicycle_data.json", "r") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)