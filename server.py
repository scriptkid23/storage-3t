from flask import Flask,send_from_directory
app = Flask(__name__)


@app.route('/uploads/<foldername>/<filename>')
def send_image(foldername,filename):
    try:
       print(filename)
       return send_from_directory("uploads/{}".format(foldername), filename)
    except:
       return 'Error'
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')