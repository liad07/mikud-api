from flask import *
import json
app = Flask(__name__)
all = open("all.txt", "r", encoding="utf8")
y = all.read()
y = y.split("\n")
d = "not found mikud"
json_dump={'error':"not insert text"}

@app.route('/', methods=['GET'])
def index(mikud="not insert mikud"):
    mikud = str(request.args.get('mikud'))
    for i in range(len(y)):
        if mikud in y[i]:
            d = y[i]
            json_dump={'city':d.split(',')[0],'street':d.split(',')[1],'numhouse':d.split(',')[2],'mikud':d.split(',')[3]}
            break
        else:
            pass
    return json_dump


app.run(host='0.0.0.0', port=80)
