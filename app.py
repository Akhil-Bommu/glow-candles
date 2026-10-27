from flask import Flask, jsonify, render_template

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Vanilla Dream", "scent": "Vanilla", "price": 299},
    {"id": 2, "name": "Lavender Calm", "scent": "Lavender", "price": 349},
    {"id": 3, "name": "Sandalwood Glow", "scent": "Sandalwood", "price": 399},
    {"id": 4, "name": "Jasmine Night", "scent": "Jasmine", "price": 329},
]


@app.route("/")
def home():
    return render_template("index.html", products=PRODUCTS)


@app.route("/api/products")
def products():
    return jsonify(PRODUCTS)


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)