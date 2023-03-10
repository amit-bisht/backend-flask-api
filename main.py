from flask import Flask,jsonify
import requests
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


@app.route("/api/user/<userid>",methods=["GET"])
def userInfo(userid):
    print("user info executed")
    headers={
        'Authorization':'Bearer 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'
    }
    try:
        url="https://api.github.com/users/"+userid
        responseAPI=requests.get(url)
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
        url="https://api.github.com/users/"+userid+"/repos"
        responseAPI=requests.get(url)
        data=json.loads(responseAPI.text)
        responseAPI.raise_for_status()
        return jsonify(data),200
    except requests.exceptions.HTTPError as err:
        return jsonify(data),404

@app.route('/')
def serve():
    return jsonify({
        "API link for fetching user info":'https://backend-flask-api.vercel.app/api/user/<user-name>',
        "API link for fetching user repos":'https://backend-flask-api.vercel.app/api/repos/<username>'
    })

if(__name__=='__main__'):
    app.run(debug=True)