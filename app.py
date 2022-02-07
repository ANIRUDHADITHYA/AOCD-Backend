from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/db/',methods=['GET','POST'])
def predict_alerts():
    response = {
        'status': 200,
        'message': 'OK',
        'db': ""
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)