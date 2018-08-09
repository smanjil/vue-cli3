
import os
from flask import Flask, request
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/ano/Documents/vue3/real-world-vue/api/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

CORS(app, resources = {r"/api/*" : {"origins" : "*"}}, headers=['Content-Type'])


@app.route('/api/post', methods = ['POST'])
@cross_origin()
def upload_file():
    file = request.files['file']

    filename = secure_filename(file.filename)
    print (filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return 'Worked'


if __name__ == '__main__':
    app.run(debug=True)
