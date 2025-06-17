from flask import Flask, request, json, jsonify
from flask import render_template
import os

app = Flask(__name__)

Directory_path = r"C:\Users\venka\OneDrive\Desktop\All files\Learn Python"


@app.route('/listoffiles')
def webpage():
     return render_template('contents.html', filenames=os.listdir(Directory_path))

@app.route('/info/json')
def json_file_transfer():

    with open(r"c:\Users\venka\OneDrive\Desktop\All files\Learn Python\JSON\api_records.json", "r", encoding = "utf-8") as f:
        data = json.load(f)
        print(json.dumps(data)) #to avoid the length in terminal I didn't use indent=2. but using it provides good readability
        return jsonify(data)
    
@app.route('/info')
def list_of_files():
    files = os.listdir(Directory_path) #os.listdir is the python built-in function to return the list of files from the directory
    return jsonify(files)
    
@app.route('/info/<filename>') #here i am passing the filename as parameter
def read_file(filename):
    #here os.listdir.join redirects to whole path of that particular file
    file_path = os.path.join(Directory_path, filename) 
    if filename in os.listdir(Directory_path): #now it gonna take the path
        #opens the file and read the content and store them in f
        with open(file_path, 'r') as f:
                #it reads all the content that present in that file
                file_content = f.read()
                print(file_content)
                return file_content  #this gives the file content. this is not json data. so, that's why we have to do this

    else:
        print("filename is not listed in the directory")
    return jsonify({"error": "File not found"}), 404


if __name__ == '__main__':
    app.run(debug=True, threaded=True, port = 7000)