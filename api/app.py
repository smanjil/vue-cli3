from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

CORS(app, resources = {r"/api/*" : {"origins" : "*"}}, headers=['Content-Type'])


@app.route('/api/post', methods = ['POST'])
@cross_origin()
def get_sensor_data():
    print (request.files['file'])
    return 'Worked'


if __name__ == '__main__':
    app.run(debug=True)
