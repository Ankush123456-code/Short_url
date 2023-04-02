from Model.Model import Model
from flask import Flask, jsonify, request, redirect, abort
import shortuuid

db = Model()


def Short_Url():
    long_url = request.json['long_url']
    short_id = shortuuid.uuid()[:6]
    short_url = request.host_url + short_id
    data = db.Is_Available({"long_url": long_url})
    if data is not None:
        details = {'long_url': long_url, 'short_url': request.host_url + f"{data['short_id']}"}
        return jsonify([{"Message": "Already present"}, details])
    db.insert_one({'long_url': long_url, 'short_id': short_id})
    return jsonify({'short_url': short_url})


def redirect_url(short_id):
    url = db.find({'short_id': short_id})
    if url == 300:
        return jsonify({"message": "Not present"})
    # return redirect(url['long_url'])
    return jsonify({"main_URL": url["long_url"]})
