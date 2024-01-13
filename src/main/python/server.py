# An object of Flask class is our WSGI application.
from flask import Flask, make_response
from flask import request
from zipfile import ZipFile
import os, shutil
import subprocess



def rmProject():
    folder = '/mnt/d/Personal/Checker/src/main/java/org/example'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def mvnTest():
    proc = subprocess.Popen('mvn test', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True, cwd="/mnt/d/Personal/Checker")

    stdout, stderr = proc.communicate()
    print(stdout, stderr)

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/', methods=['POST'])
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    file = request.files['test']
    zip_handle = ZipFile(file._file)
    zip_handle.extractall("/mnt/d/Personal/Checker/src/main/java/org/example")
    zip_handle.close()
    mvnTest()
    rmProject()
    return make_response("", 200)
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()

