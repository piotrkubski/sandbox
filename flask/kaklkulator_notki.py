from flask import Flask, abort, request
from flask.json import jsonify
app = Flask(__name__)

@app.route("/")
def index():
    return '<h1> Mój notatnik </h1>'

@app.route('/notes', methods=['GET', 'POST'])
def notes():
    return jsonify({"notes": []})

@app.route("/calculator", methods=["POST"])
def calculator():
    data = request.get_json()
    operacje = {"add": lambda a, b: a + b, "sub": lambda a, b: a - b, "mul": lambda a, b: a * b,
                "div": lambda a, b: a / b}
    if not data:
        return jsonify({"error": "brak danych"}), 400
    if data['operation'] not in operacje:
        return jsonify({"error": "bledna operacja"}), 400
    try:
        wynik = operacje[data['operation']](data['a'], data['b'])
    except ZeroDivisionError:
        return jsonify({"error": "dzielenie przez 0"}), 400
    return jsonify({"result": wynik}), 200


if __name__ == "__main__":
    app.run(debug=True)
