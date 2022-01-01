from flask import Flask,send_from_directory
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/upload/<foldername>/<filename>')
def send_image(foldername,filename):
    try:
       print(filename)
       return send_from_directory("upload/{}".format(foldername), filename)
    except:
       return 'Error'
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
