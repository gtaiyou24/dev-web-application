from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/get')
def get():
    return jsonify({
        'first_name': 'taiyo',
        'last_name': 'tamura'
    })

@app.route('/post', methods=["POST"])
def post() -> str:
    return jsonify({
        'first_name': request.json["first_name"],
        'last_name': 'tamura'
    })


if __name__ == "__main__":
    app.run(port=8080, debug=True)
