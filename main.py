from flask import *
from flask import request
from flask_cors import CORS

import json
all = open("all.txt", "r", encoding="utf8")
app = Flask(__name__)
y = all.read()
y = y.split("\n")
d = "not found mikud"
json_dump={'error':"not insert text"}
CORS(app)


@app.route('/', methods=['GET'])
def index(mikud=None):
    mikud = str(request.args.get('mikud'))

   #print(city,street,numhouse)
    for i in range(len(y)):
        if mikud == y[i].split(",")[3]:
            d = y[i]
            json_dump={'city':d.split(',')[0],'street':d.split(',')[1],'numhouse':d.split(',')[2],'mikud':d.split(',')[3].replace("\r","")}
            break
        else:
            pass
    return json_dump


app.run(host='0.0.0.0', port=80)
