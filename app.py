from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.aftercovid


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/save_venues', methods=["GET"])
def save_venues():
    return jsonify({'result': 'success'})

@app.route('/', methods=["POST"])
def bookmark():
    return jsonify({'result': 'success', 'msg': 'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)