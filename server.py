from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from collections import defaultdict
import csv
import json

app = Flask(__name__)
api = Api(app)

CORS(app)

@app.route("/")
def hello():
    with open('file1.csv', 'r') as file1:
       csv_reader = csv.reader(file1)
       next(csv_reader)
       line_count = len(list(csv_reader))
    return jsonify(line_count)

class rowsum(Resource):
    def get(self):
        with open('file1.csv', 'r') as main_file:
            newlist = csv.DictReader(main_file)

            total = 0
            for dct in newlist:
                nums = dct['SR_ID']
                newnums = nums.lstrip('AA0')
                total += int(newnums)
                answer = total/30144
        return jsonify(answer)

class All_IDs(Resource):
    def get(self):
        mapping = defaultdict(list)
        with open('file1.csv', 'r') as reader:
            allrows = csv.DictReader(reader)
            for row in allrows:
                mapping[row['CUSTOM_ID']].append(row['SR_ID'])
            # for custom_id, sr_id_list in mapping.items():
            #     result = ('{}: {}'.format(custom_id, ' | '.join(sr_id_list)))
        return jsonify(mapping)

api.add_resource(rowsum, '/rowtotal')
api.add_resource(All_IDs, '/alldata')


if __name__ == '__main__':
     app.run(port=5002)