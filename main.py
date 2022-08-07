import requests
from bs4 import BeautifulSoup
from flask import *
from flask_cors import CORS

import json
app = Flask(__name__)
CORS(app)
@app.route('/', methods=['GET'])
def index(city="not insert city"):
    city = str(request.args.get('city'))
    url=f"https://www.google.com/search?q=wether in {city}"
    r=requests.get(url)
    s=BeautifulSoup(r.text,"html.parser")
    wether=s.find("div",class_="BNeawe").text
    info=s.find("div",class_="BNeawe tAd8D AP7Wnd").text
    json_dump={"city":city,"wether":wether,"info":info.split("\n")[1]}
    return json_dump
app.run(host='0.0.0.0', port=80)
