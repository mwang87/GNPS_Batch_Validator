# views.py
from flask import abort, jsonify, render_template, request, redirect, url_for, send_file, make_response

from app import app
from models import *

import os
import csv
import json
import uuid
import requests
import batch_validator

@app.route('/', methods=['GET'])
def renderhomepage():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def validate():
    request_file = request.files['file']

    local_filename = os.path.join(app.config['UPLOAD_FOLDER'], str(uuid.uuid4()))
    request_file.save(local_filename)

    pass_validation, failures, errors_list, valid_rows, total_rows = batch_validator.perform_validation(local_filename)

    validation_dict = {}
    validation_dict["status"] = pass_validation
    validation_dict["errors"] = errors_list
    validation_dict["stats"] = []

    validation_dict["stats"].append({"type":"total_rows", "value":total_rows})
    validation_dict["stats"].append({"type":"valid_rows", "value":len(valid_rows)})

    try:
        os.remove(local_filename)
    except:
        print("Cannot Remove File")

    return json.dumps(validation_dict)


@app.route('/heartbeat', methods=['GET'])
def testapi():
    return_obj = {}
    return_obj["status"] = "success"
    return json.dumps(return_obj)
