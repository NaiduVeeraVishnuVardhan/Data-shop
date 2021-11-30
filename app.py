#!flask/bin/python
import json
import os

from flask import Flask, jsonify, abort, redirect, url_for
from flask import make_response
from flask import request
from model import mapper
import pandas as pd
from awsS3 import S3

app = Flask(__name__)

available_analysis = [
    {
        'available_analysis': ["model1", "model2", "model3"]
    }
]

@app.route('/analysis', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': available_analysis})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def parseCSV(filePath):
    col_names = ['first_name', 'last_name', 'address', 'street', 'state', 'zip']
    csvData = pd.read_csv(filePath, names=col_names, header=None)
    # Loop through the Rows
    for i, row in csvData.iterrows():
        print(i, row['first_name'], row['last_name'], row['address'], row['street'], row['state'], row['zip'], )


@app.route("/analysis/model1", methods=['POST'])
def uploadFiles():
    analysis_detail = mapper.get_model_inputs('model1')                         #Extracting the model details [bucket, key, endpoint] .
    uploaded_file = request.files['file']
    print(uploaded_file.filename)
    if uploaded_file.filename != '':
        file_path = uploaded_file.filename
        uploaded_file.save(file_path)
        parseCSV(file_path)

    S3.upload_file(analysis_detail['bucket'], analysis_detail['key'],file_path)  #Uploading the csv to specified S3 bucket.

    return jsonify({'analysis_details': analysis_detail}), 200


if __name__ == '__main__':
    app.run(debug=True)
