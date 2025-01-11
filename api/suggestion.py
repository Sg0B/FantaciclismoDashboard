from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/suggestion', methods=['GET'])
def get_suggestion():
    return jsonify({"suggestion": "Schiera Pogačar per la prossima gara!"})

if __name__ == '__main__':
    app.run()
