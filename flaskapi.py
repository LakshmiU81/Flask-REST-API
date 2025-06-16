from flask import Flask
from flask import render_template, send_from_directory
import os

app = Flask(__name__)

Directory_path = r"C:\Users\venka\OneDrive\Desktop\All files\Learn Python"


@app.route('/listoffiles')
def list_of_files():
     filenames=os.listdir(Directory_path)
     return render_template('contents.html', files=filenames )
    
@app.route('/listoffiles/<path:filename>')
def read_file(filename):
    return send_from_directory(os.path.abspath(Directory_path), filename, as_attachment=False)
#here for attachment i went with flase otherwise it gonna download all the contents of the files

if __name__ == '__main__':
    app.run(debug=True, threaded=True, port = 7000)


