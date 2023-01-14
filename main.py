from flask import Flask,jsonify
import requests
from flask_cors import CORS,cross_origin
from flask.helpers import send_from_directory
import json

app = Flask(__name__,static_folder='frontend/dist/frontend',static_url_path='')
CORS(app)


@app.route("/api/user/<userid>",methods=["GET"])
def userInfo(userid):
    print("user info executed")
    headers={
        'Authorization':'Bearer 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'
    }
    try:
        url="https://api.github.com/users/"+userid
        responseAPI=requests.get(url,headers=headers)
        data=json.loads(responseAPI.text)
        responseAPI.raise_for_status()
        return jsonify(data),responseAPI.status_code
    except requests.exceptions.HTTPError as err:
        return jsonify(data),responseAPI.status_code

@app.route("/api/repos/<userid>",methods=["GET"])
def userRepos(userid):
    print("user repos executed")
    headers={
        'Authorization':'Bearer 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'
    }
    try:
        url="https://api.github.com/users/"+userid+"/repos?per_page=4"
        responseAPI=requests.get(url,headers=headers)
        data=json.loads(responseAPI.text)
        responseAPI.raise_for_status()
        return jsonify(data),200
    except requests.exceptions.HTTPError as err:
        return jsonify(data),404

@app.route('/')
def serve():
    return send_from_directory(app.static_folder,'index.html')

if(__name__=='__main__'):
    app.run(debug=True)