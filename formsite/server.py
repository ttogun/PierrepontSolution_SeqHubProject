from flask import request
from flask import Flask
from flask import send_file
from tinydb import TinyDB, Query
import os
import random
db = TinyDB('db.json')

app = Flask(__name__)

UPLOADFOLDER = "resumes"


@app.route('/', methods=['GET'])
def index():
    return open('index.html').read()


@app.route('/form', methods=['GET'])
def formPage():
    return open('form.html').read()


@app.route('/formSubmit', methods=['POST'])
def formSubmit():
    rData = dict(request.form)
    resumeFile = request.files['resume']
    fileExt = os.path.splitext(resumeFile.filename)[1]
    fileName = rData['firstName'] + '-' + rData['lastName'] + '-' + ''.join(
        [random.choice('0123456789ABCDEF') for x in range(10)]) + fileExt

    rData['resume'] = fileName
    db.insert(rData)
    resumeFile.save(os.path.join(UPLOADFOLDER, fileName))
    return ("OK")
